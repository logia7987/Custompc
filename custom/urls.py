from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', custom_new, name='custom_edit'),
    url(r'^custom/$', CustomListView.as_view(), name='customlist'),
    url(r'^custom/(?P<pk>\d+)/$', CustomDetailView.as_view(),name='customdetail'),
]