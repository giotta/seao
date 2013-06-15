from django.conf.urls import patterns, include, url
from .api.resources import AvisResource
from django.contrib import admin


admin.autodiscover()
avis_resource = AvisResource()


urlpatterns = patterns(
    '',
    url(r'^api/', include(avis_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
