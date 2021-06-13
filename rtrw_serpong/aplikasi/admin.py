from django.contrib import admin


from . import models

class BaseAuditedModelAdmin(admin.ModelAdmin):

    def get_name(self, obj):
        return obj.biodata.nama_lengkap
    
    list_display = ('biodata', 'get_name', )
    readonly_fields = ('created_at', 'created_by',
                       'updated_at', 'updated_by', )
    # Override username as created_at and updated_at
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = f"{request.user.username}"

        else:
            obj.updated_by = f"{request.user.username}"

        super().save_model(request, obj, form, change)


@admin.register(models.Penduduk)
class PendudukAdmin(BaseAuditedModelAdmin):
    autocomplete_fields = ('biodata', )
