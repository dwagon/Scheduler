#! /usr/bin/env python
from fabric.api import task, env, sudo, runs_once, settings, hide, put
from fabric.api import cd
from fabric.contrib.files import exists
import os

env.use_ssh_config = True

basedir = '/opt/scheduler'


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


@task
def install_nginx():
    install_pkg('nginx')
    avail = '/etc/nginx/sites-available'
    enabled = '/etc/nginx/sites-enabled'
    put('configs/nginx.conf', '%s/scheduler.conf' % avail, use_sudo=True)
    if not exists('%s/scheduler.conf' % enabled):
        sudo('/bin/ln -s %s/scheduler.conf %s/scheduler.conf' % (avail, enabled))


@task
def install_virtualenv():
    install_pkg('python-virtualenv')
    install_pkg('python-dev')
    if not exists(os.path.join(basedir, 'bin/python')):
        sudo('/usr/bin/virtualenv %s' % basedir)
    with cd(basedir):
        with settings(hide('output')):
            sudo('./bin/pip install -r ./requirements.txt')


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
    install_nginx()
    install_postgres()
    clone(branch)
    install_virtualenv()

# EOF
