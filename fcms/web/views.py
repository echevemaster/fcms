from django.shortcuts import render_to_response


def index(request):
    """
    Site index
    """
    return render_to_response('index.html')
