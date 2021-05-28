from django.contrib import admin
from .models import Agama, Gelar, GolonganDarah, HubunganKeluarga, JenisKelamin, Pekerjaan, Pendidikan, PenyandangCacat, StatusKawin


def auto_list_display(model):
    audit_fields = ['created_at', 'created_by', 'updated_at', 'updated_by', ]
    try:
        list_fields = [col.name for col in model._meta.get_fields()
                       if col.name not in audit_fields]
        list_fields += audit_fields
    except:
        list_fields = [col.name for col in model._meta.get_fields()]

    return list_fields


class BaseAuditedModelAdmin(admin.ModelAdmin):
    list_display_links = ('nama', )
    search_fields = ('nama', )
    readonly_fields = ('created_at', 'created_by',
                       'updated_at', 'updated_by', )
    # Override username as created_at and updated_at

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = f"{request.user.username}"

        else:
            obj.updated_by = f"{request.user.username}"

        super().save_model(request, obj, form, change)


@admin.register(Agama)
class AgamaAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(Agama)


@admin.register(Gelar)
class GelarAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(Gelar)


@admin.register(GolonganDarah)
class GolonganDarahAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(GolonganDarah)


@admin.register(HubunganKeluarga)
class HubunganKeluargaAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(HubunganKeluarga)


@admin.register(JenisKelamin)
class JenisKelaminAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(JenisKelamin)


@admin.register(Pekerjaan)
class PekerjaanAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(Pekerjaan)


@admin.register(Pendidikan)
class PendidikanAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(Pendidikan)


@admin.register(PenyandangCacat)
class PenyandangCacatAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(PenyandangCacat)


@admin.register(StatusKawin)
class StatusKawinAdmin(BaseAuditedModelAdmin):
    list_display = auto_list_display(StatusKawin)
