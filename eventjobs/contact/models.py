from django.db import models
from rest_framework import serializers


# #################
# ##### MODEL #####
# #################

class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  phone = models.CharField(max_length=255)

  def __unicode__(self):
    return self.name


# ######################
# ##### SERIALIZER #####
# ######################

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'phone')
