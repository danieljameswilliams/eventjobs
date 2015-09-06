# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrole',
            name='event',
            field=models.ForeignKey(related_name='EventRole_event', default=None, to='event.Event'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='eventrole',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='eventshift',
            name='role',
            field=models.ForeignKey(related_name='EventShift_role', blank=True, to='event.EventRole', null=True),
        ),
    ]
