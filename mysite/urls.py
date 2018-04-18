from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url('^', include('custom.urls', namespace='custom')),
    url(r'^manager/$', ManagerHome.as_view(), name='manager_page'),
    # object compa
    url(r'^manager/compatible/$', ManagerCompaList.as_view(), name='manager_compa_list'),
    url(r'^manager/compatible/new$', ManagerCompaNew.as_view(), name='manager_compa_new'),
    url(r'^manager/compatible/(?P<pk>\d+)/edit$', ManagerCompaEdit.as_view(), name='manager_compa_edit'),
    url(r'^manager/compatible/(?P<pk>\d+)/remove$', manager_compa_remove, name='manager_compa_remove'),
    # object hardware
    url(r'^manager/hardware/$', ManagerHardwareList.as_view(), name='manager_hardware_list'),
    url(r'^manager/hardware/new$', ManagerHardwareNew.as_view(), name='manager_hardware_new'),
    url(r'^manager/hardware/(?P<pk>\d+)/edit$', ManagerHardwareUpdate.as_view(), name='manager_hardware_edit'),
    url(r'^manager/hardware/(?P<pk>\d+)/remove$', manager_hardware_remove, name='manager_hardware_remove'),
    #user
    url(r'^manager/user/$', ManagerUserList.as_view(), name='manager_user_list'),
    #stat
    url(r'^manager/stat$', ManagerStat.as_view(),name='manager_stat'),
    url(r'^getcompa', get_compa, name='get_compa'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/register/$', RegisterView.as_view(), name='register'),
    # url(r'^accounts/register/done$', RegisterDoneView.as_view(), name='register_done'),
    url(r'^admin/', admin.site.urls),
]
