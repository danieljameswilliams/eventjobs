# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_event_shifts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='rsvp',
            new_name='rsvp_at',
        ),
        migrations.RemoveField(
            model_name='eventshift',
            name='event',
        ),
    ]
