#! /usr/bin/env python
from fabric.api import task, env, sudo, runs_once, settings, hide, put
from fabric.api import cd, run
from fabric.contrib.files import exists
import os

env.use_ssh_config = True

basedir = '/opt/scheduler'
rundir = os.path.join(basedir, 'run')
logdir = os.path.join(basedir, 'logs')
bindir = os.path.join(basedir, 'bin')
staticdir = os.path.join(basedir, 'static')
user = 'scheduler'


@runs_once
def get_pkglist():
    pkgs = []
    with settings(hide('output')):
        # sudo('/usr/bin/apt-get update')
        output = sudo('COLUMNS=999 /usr/bin/dpkg --list')
    for line in output.splitlines():
        if not line.strip():
            continue
        parts = line.split()
        if parts[0] == 'ii':
            pkgs.append(parts[1])
    return pkgs


def users():
    if not run('getent group webapps', warn_only=True):
        sudo('groupadd --system webapps')
    if not run('getent passwd %s' % user, warn_only=True):
        sudo('useradd --system --gid webapps --shell /bin/bash --home %s %s' % (basedir, user))


def install_pkg(pkgname):
    installed = get_pkglist()
    if pkgname in installed:
        return
    with settings(hide('output')):
        sudo('/usr/bin/apt-get -y install %s' % pkgname)


@task
def install_postgres():
    install_pkg('postgresql-9.3')
    install_pkg('postgresql-server-dev-9.3')
    with settings(warn_only=True):
        sudo('createuser %s' % user, user='postgres')
    with settings(hide('output')):
        output = sudo('psql -l', user='postgres')
    if 'scheduler' not in output:
        sudo('createdb scheduler', user='postgres')


@task
def install_nginx():
    install_pkg('nginx')
    avail = '/etc/nginx/sites-available'
    enabled = '/etc/nginx/sites-enabled'
    if not exists('%s/scheduler.conf' % avail):
        put('configs/nginx.conf', '%s/scheduler.conf' % avail, use_sudo=True)
    else:
        put('configs/nginx.conf', '%s/scheduler.conf.dist' % avail, use_sudo=True)
    if not exists('%s/scheduler.conf' % enabled):
        sudo('/bin/ln -s %s/scheduler.conf %s/scheduler.conf' % (avail, enabled))


@task
def install_virtualenv():
    install_pkg('python-virtualenv')
    install_pkg('python-dev')
    for d in (rundir, logdir, bindir):
        if not exists(d):
            sudo('mkdir %s' % d)
    sudo('chown %s %s' % (user, rundir))
    sudo('chown %s %s' % (user, logdir))
    put('configs/gunicorn_start', os.path.join(bindir, 'gunicorn_start'), use_sudo=True)
    sudo('chmod 0755 %s' % os.path.join(bindir, 'gunicorn_start'))
    if not exists(os.path.join(basedir, 'bin/python')):
        sudo('/usr/bin/virtualenv %s' % basedir)
    with cd(basedir):
        with settings(hide('output')):
            sudo('./bin/pip install -r ./requirements.txt')


@task
def warmup():
    with cd(basedir):
        sudo("%s/python ./scheduler/manage.py migrate" % bindir, user=user)
        sudo("%s/python ./scheduler/manage.py collectstatic --noinput" % bindir)


@task
def clone(branch):
    install_pkg('git')
    if exists(basedir):
        sudo('/bin/rm -r %s' % basedir)
    with settings(hide('output')):
        sudo('git clone https://github.com/dwagon/Scheduler.git %s' % basedir)
    with cd(basedir):
        sudo('git checkout %s' % branch)


@task
def deploy(branch='master'):
    users()
    install_nginx()
    install_postgres()
    clone(branch)
    install_virtualenv()
    warmup()
    start()


@task
def start():
    with cd(basedir):
        with settings(sudo_user=user):
            sudo('touch %s/gunicorn.log' % logdir)
            sudo("%s/gunicorn_start >> %s/gunicorn.log 2>&1 & " % (bindir, logdir))
        sudo("/etc/init.d/nginx reload")

# EOF
