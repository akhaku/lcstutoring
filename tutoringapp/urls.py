from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', 'account.views.home_page'),
        url(r'^login/$', 'account.views.login_page' ),
        url(r'^account/', include('tutoringapp.account.urls') ),
        url(r'^tutors/', include('tutoringapp.tutors.urls') ),
        url(r'^tutees/', include('tutoringapp.tutees.urls') ),
        # Serve static assets for dev
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
