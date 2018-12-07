from django.conf.urls import url
from basic import views

from rest_framework import routers


urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^api/$',views.AVItemList.as_view(),
        name=views.AVItemList.name),
    url(r'^api/(?P<pk>[0-9]+)$',
        views.AVItemDetail.as_view(),
        name = views.AVItemDetail.name),
]
