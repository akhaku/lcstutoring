from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

def home_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.home_page',
                args=[]))
    return render_to_response('login.html', {},
            context_instance=RequestContext(request))

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

def logout_page(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return HttpResponseRedirect(reverse('account.views.login_page',
        args=[]))
