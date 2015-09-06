from django.db import models
from rest_framework import serializers

class Location(models.Model):
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  latitude = models.CharField(max_length=50)
  longitude = models.CharField(max_length=50)

  def __unicode__(self):
    return self.address


# #######################
# ##### SERIALIZERS #####
# #######################

class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'address', 'city', 'latitude', 'longitude')
