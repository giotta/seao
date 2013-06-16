from tastypie.resources import ModelResource
from .models import Avis


foreign_choice_values = [
    'province',
    'pays',
    'type',
    'nature',
    'disposition_non_municipale',
    'disposition_municipale',
    ]

many_to_many_choice_values = [
    'regions_livraison',
    ]


class AvisResource(ModelResource):
    def dehydrate(self, bundle):
        for val in foreign_choice_values:
            attr = getattr(bundle.obj, val)
            bundle.data[val] = (
                attr.name if attr else None)
        for val in many_to_many_choice_values:
            attrs = (getattr(bundle.obj, val)
                     .all().values_list('name', flat=True))
            bundle.data[val] = (
                ', '.join(attrs))
        return bundle

    class Meta:
        allowed_method = ['get']
        queryset = (Avis.objects.all()
                    .select_related(*foreign_choice_values)
                    .select_related(*[
                    x + '__name' for x in
                    many_to_many_choice_values]))
        resource_name = 'avis'


