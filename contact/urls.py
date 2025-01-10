from django.urls import path, re_path
from .views import ContactView


urlpatterns = [
    re_path(r'^$',
        ContactView.as_view(),
        name='contact'),
]
