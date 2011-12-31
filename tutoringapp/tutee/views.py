from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tutee.forms import TuteeForm

def register(request):
    form = TuteeForm
    return render_to_response('register_tutee.html',
            {'form':form},
            context_instance=RequestContext(request))

def add_tutee(request):
    form = TuteeForm(data=request.POST)
    if form.is_valid():
        tutee = form.save()
        messages.success(request, "Tutee successfully added")
        return HttpResponseRedirect(reverse('tutees.views.register',args=[]))
    else:
        messages.error(request, "Error adding tutee, please see errors below")
    return render_to_response('register_tutee.html',
            {'form': form },
        context_instance=RequestContext(request))

@login_required
def all_tutees(request):
    return render_to_response('all_tutees.html',{},
            context_instance=RequestContext(request))

