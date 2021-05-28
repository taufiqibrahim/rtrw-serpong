from django.db import models
from common.models import BaseModel


class Agama(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Agama'
        verbose_name_plural = 'Agama'


class Gelar(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Gelar'
        verbose_name_plural = 'Gelar'


class GolonganDarah(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Golongan Darah'
        verbose_name_plural = 'Golongan Darah'


class HubunganKeluarga(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Hubungan Keluarga'
        verbose_name_plural = 'Hubungan Keluarga'


class JenisKelamin(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Jenis Kelamin'
        verbose_name_plural = 'Jenis Kelamin'


class Pekerjaan(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Pekerjaan'
        verbose_name_plural = 'Pekerjaan'


class Pendidikan(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Pendidikan'
        verbose_name_plural = 'Pendidikan'


class PenyandangCacat(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Penyandang Cacat'
        verbose_name_plural = 'Penyandang Cacat'


class StatusKawin(BaseModel):
    nama = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        verbose_name = 'Status Kawin'
        verbose_name_plural = 'Status Kawin'
