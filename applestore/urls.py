from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'$^', views.home),
    url('cognitivo/applestore/api', views.api)
]
