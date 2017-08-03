from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name ="index" ),
    url(r'^(?P<friend_id>[0-9]+)/$', views.friend_detail, name = "friend_detail"),
    url(r'^input/$', views.input_page, name = "input_page"),
    url(r'^list/$', views.friends_list, name = "friends_list"),
    url(r'^thanks/$', views.thanks, name = "thanks")
]