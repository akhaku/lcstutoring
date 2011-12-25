from django.conf import settings
from django.core.context_processors import media as context_media

def utility(request):
    ret = {
            'MEDIA_URL': settings.MEDIA_URL,
    }
    return context_media(request)
