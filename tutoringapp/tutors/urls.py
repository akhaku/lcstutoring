from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url('^$', 'tutors.views.all_tutors')
)

