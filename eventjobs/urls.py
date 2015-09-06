from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from eventjobs.volunteer.models import VolunteerViewSet
from eventjobs.event.models import EventViewSet
from eventjobs.venue.models import VenueViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'volunteers', VolunteerViewSet)
router.register(r'event', EventViewSet)
router.register(r'venue', VenueViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls))
]