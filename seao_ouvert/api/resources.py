from tastypie.resources import ModelResource
from .models import Avis


class AvisResource(ModelResource):
    class Meta:
        queryset = Avis.objects.all()
        resource_name = 'avis'


