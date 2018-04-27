from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BoardHome.as_view(), name='board_home'),
    url(r'^new/$', views.board_new, name='board_new'),
    url(r'^list/$', views.board_list, name='board_list'),
    url(r'^list/set$', views.board_set_list, name='board_set_list'),
    url(r'(?P<pk>\d+)/detail/', views.board_detail, name='board_detail'),
    url(r'(?P<pk>\d+)/edit/', views.board_edit, name='board_edit'),
    url(r'(?P<pk>\d+)/remove/', views.board_remove, name='board_remove'),
    url(r'(?P<pk>\d+)/comment/remove/', views.board_comment_remove, name='board_comment_remove'),
]