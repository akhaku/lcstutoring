from django.shortcuts import render_to_response
from django.template import RequestContext
from match.models import Match

def all_matches(request):
    matches = Match.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_matches.html', {
        'matches': matches,
        }, context_instance=RequestContext(request))
