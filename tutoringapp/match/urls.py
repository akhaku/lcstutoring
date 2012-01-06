from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'match.views.all_matches'),
    url(r'^new/$', 'match.views.new_match'),
    url(r'^create/$', 'match.views.create_match'),
)

