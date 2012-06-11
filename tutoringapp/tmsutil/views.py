from django.http import HttpResponse
from django.core.servers.basehttp import FileWrapper
import os

def download_manual(request):
    myfile = open('static/Tutoring_Manual.pdf')
    filesize = os.path.getsize('static/Tutoring_Manual.pdf')
    response = HttpResponse(FileWrapper(myfile), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=Tutoring_Manual.pdf'
    response['Content-Length'] = filesize
    return response
