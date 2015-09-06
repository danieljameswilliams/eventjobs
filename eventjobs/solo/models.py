from django.db import models
from eventjobs.volunteer.models import Volunteer

class Solo(models.Model):
  volunteer = models.ForeignKey(Volunteer, related_name='Solo_volunteer')