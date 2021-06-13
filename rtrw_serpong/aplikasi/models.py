from django.db import models
from common.models import BaseModel
from kependudukan.models import Biodata


class Penduduk(BaseModel):
    # TYPE_TEMPAT_TINGGAL_RUMAH_MILIK_SENDIRI = 'physical'
    # TYPE_TEMPAT_TINGGAL_RUMAH_DINAS = 'virtual'
    # TYPE_TEMPAT_TINGGAL_KONTRAK = 'virtual'
    # TYPE_TEMPAT_TINGGAL_LAINNYA = 'virtual'
    # TYPE_CHOICES = (
    #     (TYPE_PHYSICAL, 'Physical'),
    #     (TYPE_VIRTUAL, 'Virtual'),
    # )
    # type = models.CharField(
    #     max_length=20,
    #     choices=TYPE_CHOICES,
    # )
    biodata = models.ForeignKey(Biodata, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Penduduk'
        verbose_name_plural = 'Penduduk'
