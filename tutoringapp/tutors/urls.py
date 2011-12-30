from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'tutors.views.register'),
    url(r'^register/$', 'tutors.views.add_tutor'),
    url(r'^all/$', 'tutors.views.all_tutors')
)

