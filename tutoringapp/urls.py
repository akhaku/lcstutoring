from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', 'account.views.login_page'),
        url(r'^accounts/', include('tutoringapp.account.urls') ),
        url(r'^auth/$', 'account.views.auth'),
        url(r'^tutors/$', 'tutors.views.all_tutors'),
        url(r'^tutors/', include('tutoringapp.tutors.urls') ),
        # Serve static assets for dev
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
