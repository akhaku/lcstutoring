from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext

@login_required
def all_tutors(request):
    return render_to_response('all_tutors.html',{},
            context_instance=RequestContext(request));
