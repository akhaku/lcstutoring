from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
        url(r'^$', 'account.views.home_page'),
        url(r'^login/$', 'account.views.login_page' ),
        url(r'^account/', include('account.urls') ),
        url(r'^tutors/', include('tutor.urls') ),
        url(r'^tutees/', include('tutee.urls') ),
        url(r'^matches/', include('match.urls') ),
        # Serve static assets for dev
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )
