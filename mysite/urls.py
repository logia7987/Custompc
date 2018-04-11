from django.conf.urls import url, include
from django.contrib import admin
from .views import *

urlpatterns = [
    url('^', include('custom.urls', namespace='custom')),
    url(r'^admin/', admin.site.urls),
    url(r'^getcompa', get_compa, name='get_compa'),
]
