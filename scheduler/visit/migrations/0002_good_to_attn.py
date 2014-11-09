# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visit',
            old_name='good',
            new_name='attn',
        ),
        migrations.AlterField(
            model_name='visit',
            name='attn',
            field=models.BooleanField(default=False, verbose_name=b'Attention Required'),
        ),
    ]
