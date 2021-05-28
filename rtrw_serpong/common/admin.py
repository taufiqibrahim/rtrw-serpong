from django.contrib import admin


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
    # Override username as created_at and updated_at
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = f"django/{request.user.username}"

        else:
            obj.updated_by = f"django/{request.user.username}"

        super().save_model(request, obj, form, change)
