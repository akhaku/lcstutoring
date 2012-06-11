from datetime import datetime
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from response.forms import ResponseForm
from response.models import Response
from response.replacements import manual_replace, tutee_replace, tutor_replace
from tutors.models import Tutor
from tutees.models import Tutee

def all_responses(request):
    responses = Response.objects.all()
    return render_to_response('response/all_responses.html', {
        'responses': responses,
        }, context_instance=RequestContext(request))

def new_response(request):
    if request.method == "POST":
        form = ResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.last_updated = datetime.now()
            response.created_by = request.user
            response.save()
            messages.success(request, "Added response")
            return HttpResponseRedirect(reverse('response.views.new_response',args=[]))
        else:
            messages.error(request, "Error adding response, please see errors below.")
    else:
        form = ResponseForm
    return render_to_response('response/new_response.html', {
        'form': form,
        }, context_instance=RequestContext(request))

def edit_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.method == "POST":
        form = ResponseForm(request.POST, instance=response)
        if form.is_valid():
            response = form.save(commit=False)
            response.last_updated = datetime.now()
            response.created_by = request.user
            response.save()
            messages.success(request, "Response saved.")
            return HttpResponseRedirect(reverse(
                'response.views.all_responses', args=[]))
        else:
            messages.error(request, "Error adding response, please see errors below.")
    else:
        form = ResponseForm(instance=response)
    return render_to_response('response/edit_response.html', {
            'form': form, 'response_id': response_id,
            }, context_instance=RequestContext(request))

def delete_response(request, response_id):
    response = get_object_or_404(Response, id=response_id)
    if request.method == "DELETE":
        response.delete()
    return HttpResponse("<h1>Success</h1>")

def respond(request):
    if request.is_ajax():
        response_id = request.GET.get('response')
        response = Response.objects.get(id=response_id).response
        tutor_id = request.GET.get('tutor')
        if tutor_id != "":
            tutor = Tutor.objects.get(id=tutor_id)
            response = tutor_replace(response, tutor)
        tutee_id = request.GET.get('tutee')
        if tutee_id != "":
            tutee = Tutee.objects.get(id=tutee_id)
            response = tutee_replace(response, tutee)
        response = manual_replace(response)
        return HttpResponse(response)
    responses = Response.objects.all()
    return render_to_response('response/respond.html', {
        'responses': responses
        }, context_instance=RequestContext(request))
