# coding: utf-8

from django.shortcuts import render, get_object_or_404

from seao_ouvert.api import models as api

def home(request):
    c = {
        'nb': api.Avis.objects.all().count(),
    }
    return render(request, 'core/home.html', c)

def avis_list(request):
    c = {
        'nb': api.Avis.objects.all().count(),
        'avis': api.Avis.objects.all()[:100]
    }
    return render(request, 'core/avis_list.html', c)

def avis_detail(request, id):
    c = {
        'avis': get_object_or_404(api.Avis, pk=id)
    }
    return render(request, 'core/avis_detail.html', c)

# footer
def legal(request):
    return render(request, 'core/legal.html')

def credits(request):
    return render(request, 'core/credits.html')
