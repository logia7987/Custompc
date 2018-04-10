from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('^', include('custom.urls', namespace='custom')),
    url(r'^admin/', admin.site.urls),
    url(r'changetojson', changeToJson, name='changetojson'),
]
