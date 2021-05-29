from django.contrib import admin
from common.admin import auto_list_display
from .models import Agama, Gelar, GolonganDarah, HubunganKeluarga, JenisKelamin, Pekerjaan, Pendidikan, PenyandangCacat, StatusKawin


class BaseAuditedModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama', )
    list_display_links = ('nama', )
    search_fields = ('nama', )
    readonly_fields = ('created_at', 'created_by',
                       'updated_at', 'updated_by', )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = f"{request.user.username}"

        else:
            obj.updated_by = f"{request.user.username}"

        super().save_model(request, obj, form, change)


@admin.register(Agama)
class AgamaAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(Gelar)
class GelarAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(GolonganDarah)
class GolonganDarahAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(HubunganKeluarga)
class HubunganKeluargaAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(JenisKelamin)
class JenisKelaminAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(Pekerjaan)
class PekerjaanAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(Pendidikan)
class PendidikanAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(PenyandangCacat)
class PenyandangCacatAdmin(BaseAuditedModelAdmin):
    pass


@admin.register(StatusKawin)
class StatusKawinAdmin(BaseAuditedModelAdmin):
    pass
