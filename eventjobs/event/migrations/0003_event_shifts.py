# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20150906_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='shifts',
            field=models.ManyToManyField(related_name='Event_shifts', to='event.EventShift'),
        ),
    ]
