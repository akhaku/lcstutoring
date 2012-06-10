from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
import json
from match.models import Match
from tmsutil.decorators import ajax_login_required
from tutors.forms import TutorForm
from tutors.models import Tutor

def register(request):
    if request.method == "POST":
        form = TutorForm(data=request.POST)
        if form.is_valid():
            tutor = form.save(commit=False)
            tutor.added_on = datetime.now()
            tutor.active = True
            tutor.save()
            messages.success(request, "Tutor successfully added.")
            return HttpResponseRedirect(reverse('tutors.views.register',args=[]))
        else:
            messages.error(request, "Error adding tutor, please see errors below.")
    else:
        form = TutorForm
    return render_to_response('register_tutor.html', {
        'form':form,
        'tutor_or_tutee': 'tutor',
        }, context_instance=RequestContext(request))

@login_required
def all_tutors(request):
    all_tutors = Tutor.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_tutors.html', {
        'tutors': all_tutors,
        }, context_instance=RequestContext(request))

@login_required
def tutors_json(request, which):
    matched_tutor_ids = Match.objects.filter(active=True).values_list('tutor_id',
            flat=True)
    if which == "hidden":
        all_tutors = Tutor.objects.filter(active=False).order_by('-added_on')
    if which == "all":
        all_tutors = Tutor.objects.filter(active=True).order_by('-added_on')
    if which == "unavailable":
        all_tutors = Tutor.objects.filter(active=True,id__in=matched_tutor_ids).\
                order_by('-added_on')
    if which == "available":
        all_tutors = Tutor.objects.filter(active=True).\
                exclude(id__in=matched_tutor_ids).order_by('-added_on')
    return render_to_response('tutors_ajax.html', {
        'tutors': all_tutors,
        }, context_instance=RequestContext(request))

@ajax_login_required
def edit_tutor(request, tutor_id=None):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    submitted = False
    if request.method == "POST":
        form = TutorForm(request.POST, instance=tutor)
        if form.is_valid():
            submitted = True
            form.save()
    else:
        form = TutorForm(instance=tutor)
    return render_to_response('edit_tutor.html',
            {'form': form, 'tutor': tutor, 'tutor_id': tutor_id,
                'submitted': submitted },
        context_instance=RequestContext(request))

@ajax_login_required
def delete_tutor(request, tutor_id=None):
    tutor = get_object_or_404(Tutor, id=tutor_id)
    if request.method == "DELETE":
        tutor.active = (tutor.active + 1)%2
        tutor.save()
    return HttpResponse("<h1>success</h1>")
