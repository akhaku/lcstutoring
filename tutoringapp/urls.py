from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'landing.views.home'),
        (r'^tutors/$', 'tutors.views.all_tutors'),
        (r'^tutors/', include('tutoringapp.tutors.urls')),
    )
