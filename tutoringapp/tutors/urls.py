from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tutors.views.all_tutors'),
    url('^$', 'tutors.views.all_tutors')
)

