from django.db import models
from eventjobs.volunteer.models import Volunteer
from eventjobs.location.models import Location

class Organization(models.Model):
  admins = models.ForeignKey(Volunteer, related_name='Organization_admins')
  volunteers = models.ManyToManyField(Volunteer)
  location = models.ForeignKey(Location, related_name='Organization_location')