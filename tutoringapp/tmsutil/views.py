from django.core.servers.basehttp import FileWrapper
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
import os

def handler404(request):
    return render_to_response('404.html', {},
            context_instance=RequestContext(request))

def handler500(request):
    return render_to_response('500.html', {},
            context_instance=RequestContext(request))

def download_manual(request):
    myfile = open('static/Tutoring_Manual.pdf')
    filesize = os.path.getsize('static/Tutoring_Manual.pdf')
    response = HttpResponse(FileWrapper(myfile), content_type="application/pdf")
    response['Content-Disposition'] = 'attachment; filename=Tutoring_Manual.pdf'
    response['Content-Length'] = filesize
    return response
