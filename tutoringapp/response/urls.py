from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'response.views.all_responses'),
    url(r'^new/$', 'response.views.new_response'),
    url(r'^create/$', 'response.views.new_response'),
    url(r'^edit/(\d+)/$', 'response.views.edit_response'),
    url(r'^delete/(\d+)/$', 'response.views.delete_response'),
    url(r'^respond/$', 'response.views.respond'),
    )
