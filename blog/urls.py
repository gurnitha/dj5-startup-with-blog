from django.urls import path, re_path

from .views import PostList, post_detail

urlpatterns = [
    re_path(r'^$',
        PostList.as_view(),
        name='blog_post_list'),
    re_path(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail,
        name='blog_post_detail'),
]
