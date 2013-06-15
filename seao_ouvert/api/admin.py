from django.contrib import admin
from .models import (
    Province,
    Type,
    Nature,
    Region,
    Disposition,
    Pays,
    UniteMontant,
    UNSPSC,
    Avis,
    Soumission,
    )

admin.site.register(Province)
admin.site.register(Type)
admin.site.register(Nature)
admin.site.register(Region)
admin.site.register(Disposition)
admin.site.register(Pays)
admin.site.register(UniteMontant)
admin.site.register(UNSPSC)
admin.site.register(Avis)
admin.site.register(Soumission)
