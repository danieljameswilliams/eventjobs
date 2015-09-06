from django.db import models
from rest_framework import serializers, viewsets
from eventjobs.contact.models import Contact

# #################
# ##### MODEL #####
# #################

class Venue(models.Model):
  name = models.CharField(max_length=255)
  contact = models.ForeignKey(Contact, related_name='Venue_contact', null=True, blank=True)

  def __unicode__(self):
    return self.name


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