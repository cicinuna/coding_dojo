from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^travels$', views.travels),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^add$', views.add),
    url(r'^process_add$', views.process_add),
    url(r'^process_join$', views.process_join),
    url(r'^travels/destination/(?P<number>\d+)$', views.show),
]
