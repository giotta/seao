# coding: utf-8

from django.shortcuts import render, get_object_or_404

from seao_ouvert.api import models as api

def home(request):
    c = {
        'nb': api.Avis.objects.all().count(),
    }
    return render(request, 'frontend/home.html', c)

def avis_list(request):
    c = {
        'nb': api.Avis.objects.all().count(),
        'avis': api.Avis.objects.all()[:100]
    }
    return render(request, 'frontend/avis_list.html', c)

def avis_detail(request, id):
    c = {
        'avis': get_object_or_404(api.Avis, pk=id)
    }
    return render(request, 'frontend/avis_detail.html', c)

# footer
def legal(request):
    return render(request, 'frontend/legal.html')

def credits(request):
    return render(request, 'frontend/credits.html')
