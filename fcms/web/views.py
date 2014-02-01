from django.shortcuts import render_to_response


def index(request):
    """
    Index site view
    """
    return render_to_response('index.html')
