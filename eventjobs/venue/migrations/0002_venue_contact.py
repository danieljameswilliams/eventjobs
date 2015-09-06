# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('venue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='contact',
            field=models.ForeignKey(related_name='Venue_contact', blank=True, to='contact.Contact', null=True),
        ),
    ]
