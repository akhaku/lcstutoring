from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
import json
from match.models import Match
from tmsutil.decorators import ajax_login_required
from tutees.forms import TuteeForm
from tutees.models import Tutee

def register(request):
    if request.method == "POST":
        form = TuteeForm(data=request.POST)
        if form.is_valid():
            tutee = form.save(commit=False)
            tutee.added_on = datetime.now()
            tutee.active = True
            tutee.save()
            messages.success(request, "Tutee successfully added.")
            return HttpResponseRedirect(reverse('tutees.views.register',args=[]))
        else:
            messages.error(request, "Error adding tutee, please see errors below.")
    else:
        form = TuteeForm
    return render_to_response('tutees/register_tutee.html', {
        'form':form,
        'tutor_or_tutee': 'tutee',
        }, context_instance=RequestContext(request))

@login_required
def all_tutees(request):
    tutees = Tutee.objects.filter(active=True).order_by('-added_on')
    return render_to_response('tutees/all_tutees.html',{
        'tutees': tutees
        }, context_instance=RequestContext(request))

def tutees_json(request, which):
    matched_tutee_ids = Match.objects.filter(active=True).values_list('tutee_id',
            flat=True)
    if which == "hidden":
        all_tutees = Tutee.objects.filter(active=False).order_by('-added_on')
    if which == "all":
        all_tutees = Tutee.objects.filter(active=True).order_by('-added_on')
    if which == "available":
        all_tutees = Tutee.objects.filter(active=True).\
                exclude(id__in=matched_tutee_ids).order_by('-added_on')
    if which == "unavailable":
        all_tutees = Tutee.objects.filter(active=True,id__in=matched_tutee_ids).\
                order_by('-added_on')
    return render_to_response('tutees/tutees_ajax.html', {
        'tutees': all_tutees,
        }, context_instance=RequestContext(request))

@ajax_login_required
def edit_tutee(request, tutee_id):
    tutee = get_object_or_404(Tutee, id=tutee_id)
    submitted = False
    if request.method == "POST":
        form = TuteeForm(request.POST, instance=tutee)
        if form.is_valid():
            submitted = True
            form.save()
    else:
        form = TuteeForm(instance=tutee)
    return render_to_response('tutees/edit_tutee.html',
            {'form': form, 'tutee_id': tutee_id, 'tutee': tutee,
                'submitted': submitted },
        context_instance=RequestContext(request))

@ajax_login_required
def delete_tutee(request, tutee_id=None):
    tutee = get_object_or_404(Tutee, id=tutee_id)
    if request.method == "DELETE":
        tutee.active = (tutee.active + 1)%2
        tutee.save()
    return HttpResponse("<h1>success</h1>")

@ajax_login_required
def search_ajax(request):
    all_tutees = Tutee.objects.filter(active=True).order_by('-added_on')
    all_tutees_json = []
    for tutee in all_tutees:
        all_tutees_json.append({'label': tutee.get_child_full_name(),
            'value': tutee.id})
    return HttpResponse(json.dumps(all_tutees_json))
