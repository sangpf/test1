from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login_handle/$', views.login_handle, name='login_handle'),
    url(r'^logout/$', views.logout, name='logout')

]

