from django.shortcuts import render_to_response
from django.template import RequestContext

def all_tutors(request):
    return render_to_response('all_tutors.html',{},
            context_instance=RequestContext(request));
