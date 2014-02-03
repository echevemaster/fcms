from django.shortcuts import render_to_response
from django.contrib.auth import logout as auth_logout
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


def index(request):
    """
    Index site view for fcms
    """
    return render_to_response('index.html')


def auth(request):
    """
    Where the users are login
    """
    return render_to_response('auth.html')


def logout(request):
    """ Logout user """
    auth_logout(request)
    return render_to_response('index.html', {}, RequestContext(request))


@login_required
def profile(request):
    return render_to_response('profile.html', {}, RequestContext(request))


def done(request):
    return render_to_response('index.html', {
        'user': request.user
    }, RequestContext(request))
