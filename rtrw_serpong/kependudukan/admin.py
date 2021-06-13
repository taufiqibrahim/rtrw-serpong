from django.contrib import admin
from common.admin import auto_list_display
from import_export.admin import ImportExportModelAdmin
from .models import Biodata, Domisili, Keluarga
from .resources import BiodataResource


class BaseAuditedModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'created_by',
                       'updated_at', 'updated_by', )
    # Override username as created_at and updated_at

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = f"{request.user.username}"

        else:
            obj.updated_by = f"{request.user.username}"

        super().save_model(request, obj, form, change)


@admin.register(Keluarga)
class KeluargaAdmin(BaseAuditedModelAdmin):
    list_display = ('no_kk', 'nama_kepala', 'alamat')
    # list_display_links = ('no_kk', )
    # search_fields = ('no_kk', 'nama_kepala', )


@admin.register(Domisili)
class DomisiliAdmin(BaseAuditedModelAdmin):
    pass


class DomisiliInlineAdmin(admin.TabularInline):
    model = Domisili
    extra = 0
    fields = ('tanggal_mulai_tinggal', 'tanggal_akhir_tinggal', )


@admin.register(Biodata)
class BiodataAdmin(BaseAuditedModelAdmin, ImportExportModelAdmin):
    resource_class = BiodataResource
    list_display = ('id', 'nama_lengkap', 'nik', )
    list_display_links = ('nama_lengkap', )
    search_fields = ('nik', 'nama_lengkap', )
    # autocomplete_fields = ('agama', )
    inlines = [DomisiliInlineAdmin, ]
