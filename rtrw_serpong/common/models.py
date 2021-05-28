from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
