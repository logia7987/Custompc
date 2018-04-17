from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', custom_new, name='custom_edit'),
    url(r'^custom/$', CustomListView.as_view(), name='custom_list'),
    url(r'^custom/(?P<pk>\d+)/$', CustomDetailView.as_view(),name='custom_detail'),
    url(r'^custom/(?P<pk>\d+)/remove/$', CustomDeleteView.as_view(), name='custom_delete'),
    url(r'^custom/(?P<pk>\d+)/comment/$', add_comment, name='add_comment'),
    url(r'^custom/(?P<pk>\d+)/comment/remove/$', comment_remove, name='comment_remove')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
