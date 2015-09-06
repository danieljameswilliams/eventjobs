from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from eventjobs.location.models import Location, LocationSerializer
from eventjobs.venue.models import Venue, VenueSerializer
from rest_framework import serializers, viewsets
from eventjobs.contact.models import Contact, ContactSerializer

PAYMENT_TYPES = (
  ('fixed', 'Fixed Salary'),
  ('hourly', 'Hourly Salary'),
  ('coupon', 'Coupon'),
  ('tickets', 'Tickets'),
  ('food', 'Food'),
  ('nothing', 'Nothing'),
  ('unknown', 'Unknown'),
  ('other', 'Other')
)


# ##################
# ##### MODELS #####
# ##################

class EventRole(models.Model):
  name = models.CharField(max_length=512)
  description = models.TextField(blank=True)
  event = models.ForeignKey('Event', related_name='EventRole_event')

  def __unicode__(self):
    return self.name

class EventShift(models.Model):
  role = models.ForeignKey(EventRole, related_name='EventShift_role', null=True, blank=True)
  quantity = models.IntegerField()
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()

  def __unicode__(self):
    return self.role.name + ': ' + self.start_at.strftime('%d-%m-%Y %H:%M') + ' - ' + self.end_at.strftime('%d-%m-%Y %H:%M')

class Event(models.Model):
  name = models.CharField(max_length=512)
  description = models.TextField(blank=True)
  location = models.ForeignKey(Location, related_name='Event_location')
  payment_type = models.CharField(choices=PAYMENT_TYPES, max_length=50)
  quantity = models.IntegerField()
  created_at = models.DateTimeField()
  created_by = models.ForeignKey(Venue, related_name='Event_created_by')
  start_at = models.DateTimeField()
  end_at = models.DateTimeField()
  rsvp_at = models.DateTimeField()
  contact = models.ForeignKey(Contact, related_name='Event_contact', null=True, blank=True)
  shifts = models.ManyToManyField(EventShift, related_name='Event_shifts')

  def __unicode__(self):
    return self.name

class EventRequest(models.Model):
  content_type = models.ForeignKey(ContentType, related_name='EventRequest_content_type')
  object_id = models.PositiveIntegerField()
  event = models.ForeignKey(Event, related_name='EventRequest_event')
  requested_for = generic.GenericForeignKey('content_type', 'object_id')
  requested_by = models.ForeignKey(User, related_name='EventRequest_user')
  created_at = models.DateTimeField()


# ######################
# ##### SERIALIZER #####
# ######################

class EventRoleSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = EventRole
    fields = ('id', 'name', 'description')

class EventShiftSerializer(serializers.HyperlinkedModelSerializer):
  role = EventRoleSerializer()

  class Meta:
    model = EventShift
    fields = ('id', 'role', 'quantity', 'start_at', 'end_at')

class EventSerializer(serializers.HyperlinkedModelSerializer):
  location = LocationSerializer()
  created_by = VenueSerializer()
  contact = ContactSerializer()
  shifts = EventShiftSerializer(many=True)

  class Meta:
    model = Event
    fields = ('id', 'url', 'name', 'description', 'contact', 'location', 'payment_type', 'quantity', 'created_at', 'created_by', 'start_at', 'end_at', 'rsvp_at', 'shifts')


# ####################
# ##### API VIEW #####
# ####################

class EventViewSet(viewsets.ModelViewSet):
  queryset = Event.objects.all()
  serializer_class = EventSerializer