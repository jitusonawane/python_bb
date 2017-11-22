from django.conf.urls import url
from django.contrib import admin
from . import views    
    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),      
    url(r'^friends$', views.friends),
    # url(r'^show/(?P<frId>\d+)$', views.profile),
    # url(r'^add_friend/(?P<usId>\d+)$', views.add_friend),
    # url(r'^remove_friend/(?P<frId>\d+)$', views.remove_friend),
    # url(r'^create$', views.additem),

    url(r'^add_item$', views.add_item),
    url(r'^add_wish/(?P<wish_id>\d+)$', views.add_wish),
    url(r'^remove_wish/(?P<wish_id>\d+)$', views.remove_wish),
    url(r'^item/(?P<item_id>\d+)$', views.item),
    url(r'^delete(?P<item_id>\d+)$', views.delete)
    
]


