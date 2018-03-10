from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_total$', views.process_total),
    url(r'^checkout$', views.checkout),
    url(r'^go_back$', views.go_back)
]
