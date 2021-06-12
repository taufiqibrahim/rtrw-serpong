from common.models import BaseModel
from djgeojson.fields import PolygonField
from django.db import models


class BidangTanah(BaseModel):
    deskripsi = models.TextField()
    picture = models.ImageField()
    geom = PolygonField()

    class Meta:
        verbose_name = 'Bidang Tanah'
        verbose_name_plural = 'Bidang Tanah'

    def __str__(self) -> str:
        return str(self.pk)

    @property
    def picture_url(self):
        return self.picture.url


class Bangunan(BaseModel):
    bidang_tanah = models.ForeignKey(
        BidangTanah, on_delete=models.PROTECT, null=False)
    alamat = models.CharField(max_length=255)
    geom = PolygonField(null=True)

    # pemilik = TODO foreign to biodata

    # uu-no-28-tahun-2002-bangunan-gedung BAB III FUNGSI BANGUNAN GEDUNG Pasal 5 direkomendasikan menjadi data master
    fungsi = models.ForeignKey(
        'master.FungsiBangunan', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Bangunan'
        verbose_name_plural = 'Bangunan'

    def __str__(self) -> str:
        if self.alamat:
            return self.alamat
        else:
            return self.pk
