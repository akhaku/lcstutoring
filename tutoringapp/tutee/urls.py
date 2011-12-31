from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tutees.views.register'),
    url(r'^register/$', 'tutees.views.add_tutee'),
    url(r'^all/$', 'tutees.views.all_tutees')
)

