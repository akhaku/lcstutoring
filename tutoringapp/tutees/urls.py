from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tutees.views.register'),
    url(r'^all/$', 'tutees.views.all_tutees'),
    url(r'^json/(\w+)/$', 'tutees.views.tutees_json'),
    url(r'^edit/$', 'tutees.views.edit_tutee'),
    url(r'^edit/(\d+)/$', 'tutees.views.edit_tutee'),
)

