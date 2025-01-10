# from django.conf.urls import url
from django.urls import path, include, re_path

from .views import ContactView


urlpatterns = [
    re_path(r'^$',
        ContactView.as_view(),
        name='contact'),
]
