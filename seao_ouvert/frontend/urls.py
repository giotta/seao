# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'seao_ouvert.frontend.views',
    url(r'^$', 'home', name='home'),
    url(r'^legal', 'legal', name='legal'),
    url(r'^avis', 'avis_list', name='avis'),
)
