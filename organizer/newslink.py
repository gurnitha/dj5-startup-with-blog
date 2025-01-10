# from django.conf.urls import url
from django.urls import path, include, re_path

from .views import (
    NewsLinkCreate, NewsLinkDelete,
    NewsLinkUpdate)

urlpatterns = [
    re_path(r'^create/$',
        NewsLinkCreate.as_view(),
        name='organizer_newslink_create'),
    re_path(r'^delete/(?P<pk>\d+)/$',
        NewsLinkDelete.as_view(),
        name='organizer_newslink_delete'),
    re_path(r'^update/(?P<pk>\d+)/$',
        NewsLinkUpdate.as_view(),
        name='organizer_newslink_update'),
]
