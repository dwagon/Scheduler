# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='duration',
            field=models.SmallIntegerField(default=0, help_text=b'Number of hours per visit'),
        ),
    ]
