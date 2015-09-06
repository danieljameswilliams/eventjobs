from django.db import models
from rest_framework import serializers, viewsets

# #################
# ##### MODEL #####
# #################

class Venue(models.Model):
  name = models.CharField(max_length=255)


# ######################
# ##### SERIALIZER #####
# ######################

class VenueSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = Venue
    fields = ('id', 'url', 'name')


# ####################
# ##### API VIEW #####
# ####################

class VenueViewSet(viewsets.ModelViewSet):
  queryset = Venue.objects.all()
  serializer_class = VenueSerializer