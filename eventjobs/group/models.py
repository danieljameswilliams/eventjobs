from django.db import models
from eventjobs.volunteer.models import Volunteer

class Group(models.Model):
  volunteers = models.ManyToManyField(Volunteer)