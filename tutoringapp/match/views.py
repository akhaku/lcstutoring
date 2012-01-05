from django.shortcuts import render_to_response
from django.template import RequestContext
from match.models import Match
from tutees.models import Tutee
from tutors.models import Tutor

def all_matches(request):
    matches = Match.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_matches.html', {
        'matches': matches,
        }, context_instance=RequestContext(request))

def new_match(request):
    matched_tutee_ids = Match.objects.filter(active=True).values_list('tutee_id',
            flat=True)
    matched_tutor_ids = Match.objects.filter(active=True).values_list('tutor_id',
            flat=True)
    available_tutors = Tutor.objects.filter(active=True).exclude(id__in=matched_tutor_ids)
    available_tutees = Tutee.objects.filter(active=True).exclude(id__in=matched_tutee_ids)
    return render_to_response('new_match.html', {
        'tutors': available_tutors,
        'tutees': available_tutees,
        }, context_instance=RequestContext(request))
