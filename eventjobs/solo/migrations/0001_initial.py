# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volunteer', models.ForeignKey(related_name='Solo_volunteer', to='volunteer.Volunteer')),
            ],
        ),
    ]
