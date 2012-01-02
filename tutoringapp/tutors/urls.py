from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^$', 'tutors.views.register'),
    url(r'^all/$', 'tutors.views.all_tutors'),
    url(r'^edit/(\d+)/$', 'tutors.views.edit_tutor'),
)
