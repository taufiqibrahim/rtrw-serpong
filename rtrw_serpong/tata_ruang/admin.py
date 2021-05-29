from common.admin import BaseAuditedLeafletGeoModelAdmin
from django.contrib import admin


from . import models as tata_ruang_models

# admin.site.register(tata_ruang_models.BidangTanah, LeafletGeoAdmin)
@admin.register(tata_ruang_models.BidangTanah)
class BidangTanahAdmin(BaseAuditedLeafletGeoModelAdmin):
    pass