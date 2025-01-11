# from django.conf.urls import url
from django.urls import path, include, re_path

from ..views import (
    NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate, StartupCreate, StartupDelete,
    StartupDetail, StartupList, StartupUpdate)

urlpatterns = [
    re_path(r'^$',
        StartupList.as_view(),
        name='organizer_startup_list'),
    re_path(r'^create/$',
        StartupCreate.as_view(),
        name='organizer_startup_create'),
    re_path(r'^(?P<slug>[\w\-]+)/$',
        StartupDetail.as_view(),
        name='organizer_startup_detail'),
    re_path(r'^(?P<startup_slug>[\w\-]+)/'
        r'add_article_link/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    re_path(r'^(?P<slug>[\w\-]+)/delete/$',
        StartupDelete.as_view(),
        name='organizer_startup_delete'),
    re_path(r'^(?P<slug>[\w\-]+)/update/$',
        StartupUpdate.as_view(),
        name='organizer_startup_update'),
    re_path(r'^(?P<startup_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'delete/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    re_path(r'^(?P<startup_slug>[\w\-]+)/'
        r'(?P<newslink_slug>[\w\-]+)/'
        r'update/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
]
