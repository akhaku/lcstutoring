from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def login_page(request):
    return render_to_response('login.html', {},
            context_instance=RequestContext(request));

def auth(request):
    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        messages.info(request, "Logged in as %s" % username)
        login(request, user)
    else:
        messages.error(request, "Could not log you in as %s" % username)
    return HttpResponseRedirect(reverse('account.views.login_page',args=[]))
