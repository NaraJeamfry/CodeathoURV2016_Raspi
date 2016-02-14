
from django.conf.urls import url

from django.views.generic import TemplateView

from Server.views import HomeView
from .views import ClassroomDetails, ZoneDetails, FacultyDetails, CampusDetails

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    #url(r'^$', ListCampus.as_view(), name='home'),

    url(r'^(?P<campus>\w+)/$', CampusDetails.as_view(), name='campus'),

    url(r'^(?P<campus>\w+)/(?P<faculty>\w+)/$', FacultyDetails.as_view(), name='faculty'),

    url(r'^(?P<campus>\w+)/(?P<faculty>\w+)/(?P<zone>\w+)/$', ZoneDetails.as_view(), name='zone'),

    url(r'^(?P<campus>\w+)/(?P<faculty>\w+)/(?P<zone>\w+)/(?P<classroom>\w+)/$', ClassroomDetails.as_view(),
        name='classroom'),
]