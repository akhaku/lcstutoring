from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'landing.views.home'),
        (r'^tutors/$', 'tutors.views.all_tutors'),
        (r'^tutors/', include('tutoringapp.tutors.urls')),
        # Serve static assets for dev
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
