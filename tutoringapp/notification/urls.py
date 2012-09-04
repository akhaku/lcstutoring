
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^all/(\d+)/$', 'notification.views.view_notifications'),
)
