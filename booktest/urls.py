from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    # url(r'^([0-9]+)/$', views.detail),
    # url(r'^book/([0-9]+)/$', views.detail),
    url(r'^book/([0-9]+)/$', views.detail, name="detail"),

    url(r'^getTest1/$', views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),

    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$',views.postTest2),

    url(r'^response_index/$', views.response_index),

    url(r'^json_index/$', views.json_index),


]

