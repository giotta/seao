# coding: utf-8

from django.shortcuts import render

from seao_ouvert.api import models as api

def home(request):
    c = {
        'nb': api.Avis.objects.all().count(),
    }
    return render(request, 'frontend/home.html', c)

def legal(request):
    return render(request, 'frontend/legal.html')

def avis_list(request):
    c = {
        'nb': api.Avis.objects.all().count(),
        'avis': api.Avis.objects.all()[:100]
    }
    return render(request, 'frontend/avis.html', c)
