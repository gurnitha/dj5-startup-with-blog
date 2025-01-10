# from django.conf.urls import url
from django.urls import path, include, re_path

from .views import (
    StartupCreate, StartupDelete, StartupList,
    StartupUpdate, startup_detail)

urlpatterns = [
    re_path(r'^$',
        StartupList.as_view(),
        name='organizer_startup_list'),
    re_path(r'^create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    re_path(r'^(?P<slug>[\w\-]+)/$',
        startup_detail,
        name='organizer_startup_detail'),
    re_path(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    re_path(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
]
