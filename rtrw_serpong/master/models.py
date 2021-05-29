from django.db import models
from common.models import BaseModel


class MasterModel(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        abstract = True
        ordering = ['id', ]

    def __str__(self) -> str:
        return self.nama


class Agama(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Agama'
        verbose_name_plural = 'Agama'


class Gelar(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Gelar'
        verbose_name_plural = 'Gelar'


class GolonganDarah(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Golongan Darah'
        verbose_name_plural = 'Golongan Darah'


class HubunganKeluarga(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Hubungan Keluarga'
        verbose_name_plural = 'Hubungan Keluarga'


class JenisKelamin(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Jenis Kelamin'
        verbose_name_plural = 'Jenis Kelamin'


class Pekerjaan(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Pekerjaan'
        verbose_name_plural = 'Pekerjaan'


class Pendidikan(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Pendidikan'
        verbose_name_plural = 'Pendidikan'


class PenyandangCacat(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Penyandang Cacat'
        verbose_name_plural = 'Penyandang Cacat'


class StatusKawin(MasterModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Status Kawin'
        verbose_name_plural = 'Status Kawin'
