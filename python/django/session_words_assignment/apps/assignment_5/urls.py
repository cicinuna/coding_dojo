from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.words),
    url(r'^process_add$', views.process_add),
    url(r'^clear_session$', views.clear_session)
]