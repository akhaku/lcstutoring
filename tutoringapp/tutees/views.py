from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from match.models import Match
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
    return render_to_response('register_tutee.html', {
        'form':form,
        'tutor_or_tutee': 'tutee',
        }, context_instance=RequestContext(request))

@login_required
def all_tutees(request):
    tutees = Tutee.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_tutees.html',{
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
    return render_to_response('tutees_ajax.html', {
        'tutees': all_tutees,
        }, context_instance=RequestContext(request))

@login_required
def edit_tutee(request, tutee_id):
    tutee = get_object_or_404(Tutee, id=tutee_id)
    form = TuteeForm(instance=tutee)
    return render_to_response('register_tutee.html',
            {'form': form },
        context_instance=RequestContext(request))

