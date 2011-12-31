from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from tutees.forms import TuteeForm
from tutees.models import Tutee

def register(request):
    form = TuteeForm
    return render_to_response('register_tutee.html', {
        'form':form
        }, context_instance=RequestContext(request))

def add_tutee(request):
    form = TuteeForm(data=request.POST)
    if form.is_valid():
        tutee = form.save(commit=False)
        tutee.added_on = datetime.now()
        tutee.save()
        messages.success(request, "Tutee successfully added")
        return HttpResponseRedirect(reverse('tutees.views.register',args=[]))
    else:
        messages.error(request, "Error adding tutee, please see errors below")
    return render_to_response('register_tutee.html',
            {'form': form },
        context_instance=RequestContext(request))

@login_required
def all_tutees(request):
    tutees = Tutee.objects.filter(active=True).order_by('-added_on')
    return render_to_response('all_tutees.html',{
        'tutees': tutees
        }, context_instance=RequestContext(request))

@login_required
def edit_tutee(request, tutee_id):
    tutee = get_object_or_404(Tutee, id=tutee_id)
    form = TuteeForm(instance=tutee)
    return render_to_response('register_tutee.html',
            {'form': form },
        context_instance=RequestContext(request))

