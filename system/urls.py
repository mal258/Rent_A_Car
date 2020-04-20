from django.conf.urls import url
from django.contrib import admin
from system import views
from . import views

urlpatterns = [
    url(r'^$', views.home, name = "home"),
    url(r'^$', views.car_list, name="car_list"),

    #url(r'^carlist/$', system.views.car_list, name = "car_list"),
    url(r'^createOrder/$', views.order_created, name = "order_create"),

    url(r'^(?P<id>\d+)/edit/$', views.car_update, name = "car_edit"),


    url(r'^(?P<id>\d+)/$', views.car_detail, name = "car_detail"),
    url(r'^detail/(?P<id>\d+)/$', views.order_detail, name = "order_detail"),

    url(r'^(?P<id>\d+)/delete/$', views.car_delete, name = "car_delete"),
    url(r'^(?P<id>\d+)/deleteOrder/$', views.order_delete, name = "order_delete"),

    url(r'^contact/$', views.contact, name = "contact"),

    url(r'^newcar/$', views.newcar, name = "newcar"),
    url(r'^(?P<id>\d+)/like/$', views.like_update, name = "like"),
    url(r'^popularcar/$', views.popular_car, name = "popularcar"),
    url(r'^location/', views.location_list, name = "location_list"),
    url(r'^addLocation/$', views.location, name = "location"),
    url(r'^(?P<id>\d+)/location/$', views.loc_detail, name = "loc_detail"),
    url(r'^(?P<id>\d+)/edit/$', views.loc_edit, name = "loc_edit"),
    url(r'^(?P<id>\d+)/delete/$', views.loc_delete, name = "loc_delete"),

]
