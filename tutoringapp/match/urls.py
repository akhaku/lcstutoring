from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'match.views.all_matches'),
    url(r'^new/$', 'match.views.new_match'),
    url(r'^create/$', 'match.views.create_match'),
    url(r'^json/$', 'match.views.matches_json'),
    url(r'^edit/$', 'match.views.edit_match'),
    url(r'^edit/(\d+)/$', 'match.views.edit_match'),
    url(r'^remove/$', 'match.views.delete_match'),
    url(r'^remove/(\d+)/$', 'match.views.delete_match'),
)

