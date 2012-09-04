from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from urllib import urlencode

def home_page(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.login_page', args=[]))
    return render_to_response('home.html', {},
            context_instance=RequestContext(request))

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('account.views.home_page',
                args=[]))
    return render_to_response('login.html', { 'redirect_to': request.GET.get('next')},
        context_instance=RequestContext(request))

def auth(request):
    username = request.REQUEST.get('username')
    password = request.REQUEST.get('password')
    user = authenticate(username=username, password=password)
    redirect_to = request.REQUEST.get('next')
    if user is not None:
        messages.info(request, "Logged in as %s" % username)
        login(request, user)
        return HttpResponseRedirect(redirect_to)
    else:
        messages.error(request, "Could not log you in as %s" % username)
    return HttpResponseRedirect("%s?%s" % (reverse('account.views.login_page',
        args=[]), urlencode(dict(next=redirect_to)) ) )

def logout_page(request):
    logout(request)
    messages.info(request, "Successfully logged out")
    return HttpResponseRedirect(reverse('account.views.login_page',
        args=[]))
