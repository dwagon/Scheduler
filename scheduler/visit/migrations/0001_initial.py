# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('good', models.BooleanField(default=True)),
                ('date', models.DateField()),
                ('note', models.CharField(max_length=250, blank=True)),
                ('client', models.ForeignKey(to='client.Client')),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='visit',
            unique_together=set([('client', 'date')]),
        ),
    ]
