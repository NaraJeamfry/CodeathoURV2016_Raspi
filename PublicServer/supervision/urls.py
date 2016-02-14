
from django.conf.urls import url

from django.views.generic import TemplateView

from Server.views import HomeView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
]