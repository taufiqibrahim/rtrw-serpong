from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Tanggal Data Dibuat", auto_now_add=True)
    created_by = models.CharField(verbose_name="Data Dibuat Oleh", max_length=50, blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name="Tanggal Data Diperbarui", auto_now=True, null=True)
    updated_by = models.CharField(verbose_name="Data Diperbarui Oleh", max_length=50, blank=True, null=True)

    class Meta:
        abstract = True
