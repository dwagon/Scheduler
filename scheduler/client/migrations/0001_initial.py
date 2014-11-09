# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200)),
                ('regularity', models.PositiveSmallIntegerField(help_text=b'How many weeks between visits')),
                ('dayofweek', models.SmallIntegerField(choices=[(0, b'Monday'), (1, b'Tuesday'), (2, b'Wednesday'), (3, b'Thursday'), (4, b'Friday'), (5, b'Saturday'), (6, b'Sunday'), (7, b'Anyday')])),
                ('duration', models.SmallIntegerField(choices=[(0, b'Unknown'), (1, b'Hour'), (2, b'1/4 Day'), (3, b'1/3 Day'), (4, b'1/2 Day'), (9, b'Full Day')])),
                ('note', models.CharField(max_length=250, blank=True)),
                ('flexible', models.BooleanField(default=False)),
                ('startdate', models.DateField(default=None, help_text=b'Schedule visits from this date (YYYY-MM-DD)', null=True)),
                ('enddate', models.DateField(default=None, help_text=b'Schedule visits until this date (YYYY-MM-DD)', null=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
