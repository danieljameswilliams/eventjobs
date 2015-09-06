from django.contrib.auth.models import User
from django.db import models
from rest_framework import serializers, viewsets
from eventjobs.location.models import Location, LocationSerializer


# #################
# ##### MODEL #####
# #################

class Volunteer(models.Model):
  name = models.CharField(max_length=200)
  user = models.OneToOneField(User)
  location = models.ForeignKey(Location, related_name='Volunteer_location')


# #######################
# ##### SERIALIZERS #####
# #######################

class UserSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'email', 'is_staff')

class VolunteerSerializer(serializers.HyperlinkedModelSerializer):
  location = LocationSerializer()
  user = UserSerializer()

  class Meta:
    model = Volunteer
    fields = ('id', 'url', 'user', 'location')


# ####################
# ##### API VIEW #####
# ####################

class VolunteerViewSet(viewsets.ModelViewSet):
  queryset = Volunteer.objects.all()
  serializer_class = VolunteerSerializer
