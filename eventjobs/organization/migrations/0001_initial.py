# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('volunteer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admins', models.ForeignKey(related_name='Organization_admins', to='volunteer.Volunteer')),
                ('location', models.ForeignKey(related_name='Organization_location', to='location.Location')),
                ('volunteers', models.ManyToManyField(to='volunteer.Volunteer')),
            ],
        ),
    ]
