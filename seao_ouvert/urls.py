from django.conf.urls import patterns, include, url
from django.contrib import admin

from .api.resources import AvisResource


admin.autodiscover()
avis_resource = AvisResource()


urlpatterns = patterns(
    '',
    url(r'^api/v1/', include(avis_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
