from datetime import datetime
import json
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from match.forms import MatchForm
from match.models import Match
from notification.models import Notification
from tmsutil.decorators import ajax_login_required
from tutees.models import Tutee
from tutors.models import Tutor

@login_required
def all_matches(request):
    matches = Match.objects.filter(active=True).order_by('-added_on')
    return render_to_response('match/all_matches.html', {
        'matches': matches,
        }, context_instance=RequestContext(request))

@login_required
def matches_json(request):
    matches = Match.objects.filter(active=True).order_by('-added_on')
    return render_to_response('match/matches_ajax.html', {
        'matches': matches,
        }, context_instance=RequestContext(request))

@login_required
def new_match(request):
    matched_tutee_ids = Match.objects.filter(active=True).values_list('tutee_id',
            flat=True)
    matched_tutor_ids = Match.objects.filter(active=True).values_list('tutor_id',
            flat=True)
    available_tutors = Tutor.objects.filter(active=True).exclude(id__in=matched_tutor_ids)
    available_tutees = Tutee.objects.filter(active=True).exclude(id__in=matched_tutee_ids)
    return render_to_response('match/new_match.html', {
        'tutors': available_tutors,
        'tutees': available_tutees,
        }, context_instance=RequestContext(request))

@ajax_login_required
def create_match(request):
    # TODO validation here
    tutee_id = request.POST.get('tutee_id')
    tutor_id = request.POST.get('tutor_id')
    match_note = request.POST.get('match_note')
    if tutee_id is None or tutor_id is None:
        message = {'error' : True,
                'message': 'Please select a tutor and tutor' }
    else:
        tutee = Tutee.objects.get(id=tutee_id) 
        tutor = Tutor.objects.get(id=tutor_id) 
        match = Match.objects.create(tutee=tutee, tutor=tutor, matcher=request.user,
                location="", added_on = datetime.now(), note=match_note)
        message = {
                'error': False,
                'tutor': match.tutor.get_full_name(),
                'tutor_id': match.tutor.id,
                'tutee': match.tutee.get_child_full_name(),
                'tutee_id': match.tutee.id}
    message = json.dumps(message)
    Notification.objects.create_match(request.user, match)
    return HttpResponse(message, mimetype='application/json')

@ajax_login_required
def edit_match(request, match_id=None):
    match = get_object_or_404(Match, id=match_id)
    submitted = False
    if request.method == "POST":
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            submitted = True
            form.save()
            Notification.objects.edit_match(request.user, match)
    else:
        form = MatchForm(instance=match)
    return render_to_response('match/edit_match.html',
            {'form': form, 'match_id': match_id, 'match': match,
                'submitted': submitted},
            context_instance=RequestContext(request))

@ajax_login_required
def delete_match(request, match_id=None):
    match = get_object_or_404(Match, id=match_id)
    if request.method == "DELETE":
        match.active = 0
        match.save()
        Notification.objects.delete_match(request.user, match)
    return HttpResponse("<h1>Success</h1>") # TODO what was I doing here?
