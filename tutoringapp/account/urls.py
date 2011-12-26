from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^login/$', 'account.views.login_page')
)

