from django.contrib import admin
from eventjobs.event.models import Event, EventRole, EventShift

admin.site.register(Event)
admin.site.register(EventRole)
admin.site.register(EventShift)