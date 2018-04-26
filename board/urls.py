from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.BoardHome.as_view(), name='board_home'),
    url(r'^list/$', views.board_list, name='board_list'),
    url(r'^list/set$', views.board_set_list, name='board_set_list'),
]