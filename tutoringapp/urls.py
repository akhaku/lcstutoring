from django.conf import settings
from django.conf.urls.defaults import *
from tmsutil import views

handler404 = 'tmsutil.views.handler404'
handler500 = 'tmsutil.views.handler500'

urlpatterns = patterns('',
        url(r'^$', 'account.views.home_page'),
        url(r'^favicon.ico(?P<path>)$', 'django.views.static.serve',
            {'document_root': "%s/img/favicon.ico" % settings.MEDIA_ROOT}),
        url(r'^manual/$', 'tmsutil.views.download_manual' ),
        url(r'^login/$', 'account.views.login_page' ),
        url(r'^account/', include('account.urls') ),
        url(r'^tutors/', include('tutors.urls') ),
        url(r'^tutees/', include('tutees.urls') ),
        url(r'^matches/', include('match.urls') ),
        url(r'^respond/', include('response.urls') ),
        # Serve static assets for dev
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
