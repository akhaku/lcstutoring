from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from tutors.forms import TutorForm

def register(request):
    regform = TutorForm
    return render_to_response('register_tutor.html',
            {'form':regform},
            context_instance=RequestContext(request))

def add_tutor(request):
    form = TutorForm(data=request.POST)
    if form.is_valid():
        tutor = form.save()
        messages.success(request, "Tutor successfully added")
        return HttpResponseRedirect(reverse('tutors.views.register',args=[]))
    else:
        messages.error(request, "Error adding tutor, please see errors below")
    return render_to_response('register_tutor.html',
            {'form': form },
        context_instance=RequestContext(request))

@login_required
def all_tutors(request):
    return render_to_response('all_tutors.html',{},
            context_instance=RequestContext(request))
