from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', GroupListView.as_view(), name='GroupListView'),
]
