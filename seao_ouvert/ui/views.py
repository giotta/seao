from django.shortcuts import render
from django.template import RequestContext

def home(request):
    return render(
        {},
        'ui/home.html',
        context_instance=RequestContext(request, {}),
        )
