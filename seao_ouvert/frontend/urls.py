# coding: utf-8

from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'seao_ouvert.frontend.views',
    url(r'^avis/$', 'avis_list', name='avis_list'),
    url(r'^avis/(?P<id>\d+)', 'avis_detail', name='avis_detail'),

    # footer
    url(r'^legal/$', 'legal', name='legal'),
    url(r'^credits/$', 'credits', name='credits'),
)
