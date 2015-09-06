# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('event', '0004_auto_20150906_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='contact',
            field=models.ForeignKey(related_name='Event_contact', blank=True, to='contact.Contact', null=True),
        ),
    ]
