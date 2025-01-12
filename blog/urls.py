from django.urls import path, re_path

from .views import (
    PostArchiveMonth, PostArchiveYear, PostCreate,
    PostDelete, PostDetail, PostList, PostUpdate)

urlpatterns = [
    re_path(r'^$',
        PostList.as_view(),
        name='blog_post_list'),
    re_path(r'^create/$',
        PostCreate.as_view(),
        name='blog_post_create'),
    re_path(r'^(?P<year>\d{4})/$',
        PostArchiveYear.as_view(),
        name='blog_post_archive_year'),
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/$',
        PostArchiveMonth.as_view(),
        name='blog_post_archive_month'),
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        PostDetail.as_view(),
        name='blog_post_detail'),
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'delete/$',
        PostDelete.as_view(),
        name='blog_post_delete'),
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/'
        r'update/$',
        PostUpdate.as_view(),
        name='blog_post_update'),
]
