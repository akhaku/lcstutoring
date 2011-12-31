from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from tutors.forms import TutorForm
from tutors.models import Tutor

def register(request):
    regform = TutorForm
    return render_to_response('register_tutor.html', {
        'form':regform
        }, context_instance=RequestContext(request))

def add_tutor(request):
    form = TutorForm(data=request.POST)
    if form.is_valid():
        tutor = form.save(commit=False)
        tutor.added_on = datetime.now()
        tutor.active = True
        tutor.save()
        messages.success(request, "Tutor successfully added")
        return HttpResponseRedirect(reverse('tutors.views.register',args=[]))
    else:
        messages.error(request, "Error adding tutor, please see errors below")
    return render_to_response('register_tutor.html',
            {'form': form },
        context_instance=RequestContext(request))

@login_required
def all_tutors(request):
    all_tutors = Tutor.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_tutors.html', {
        'tutors': all_tutors,
        }, context_instance=RequestContext(request))

@login_required
def edit_tutor(request, tutor_id):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    form = TutorForm(instance=tutor)
    return render_to_response('register_tutor.html',
            {'form': form },
        context_instance=RequestContext(request))

