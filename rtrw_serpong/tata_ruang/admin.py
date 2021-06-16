from common.admin import BaseAuditedLeafletGeoModelAdmin
from django.contrib import admin


from . import models as tata_ruang_models

# admin.site.register(tata_ruang_models.BidangTanah, LeafletGeoAdmin)


@admin.register(tata_ruang_models.BidangTanah)
class BidangTanahAdmin(BaseAuditedLeafletGeoModelAdmin):
    pass


@admin.register(tata_ruang_models.Bangunan)
class BangunanAdmin(BaseAuditedLeafletGeoModelAdmin):
    list_display = ('id', 'pemilik', 'alamat', 'fungsi',)
