from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^logout/$', 'account.views.logout_page'),
    url('^manage/$', 'account.views.management'),
    url('^auth/$', 'account.views.auth'),
    url('^changePassword/$', 'account.views.change_password'),
)

