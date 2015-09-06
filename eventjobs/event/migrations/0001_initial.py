# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venue', '__first__'),
        ('location', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
                ('payment_type', models.CharField(max_length=50, choices=[(b'fixed', b'Fixed Salary'), (b'hourly', b'Hourly Salary'), (b'coupon', b'Coupon'), (b'tickets', b'Tickets'), (b'food', b'Food'), (b'nothing', b'Nothing'), (b'unknown', b'Unknown'), (b'other', b'Other')])),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('rsvp', models.DateTimeField()),
                ('created_by', models.ForeignKey(related_name='Event_created_by', to='venue.Venue')),
                ('location', models.ForeignKey(related_name='Event_location', to='location.Location')),
            ],
        ),
        migrations.CreateModel(
            name='EventRequest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField()),
                ('content_type', models.ForeignKey(related_name='EventRequest_content_type', to='contenttypes.ContentType')),
                ('event', models.ForeignKey(related_name='EventRequest_event', to='event.Event')),
                ('requested_by', models.ForeignKey(related_name='EventRequest_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='EventShift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('start_at', models.DateTimeField()),
                ('end_at', models.DateTimeField()),
                ('event', models.ForeignKey(related_name='EventShift_event', to='event.Event')),
                ('role', models.ForeignKey(related_name='EventShift_role', to='event.EventRole')),
            ],
        ),
    ]
