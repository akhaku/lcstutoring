from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tutees.views.register'),
    url(r'^all/$', 'tutees.views.all_tutees'),
    url(r'^edit/(\d+)/$', 'tutees.views.edit_tutee'),
)

