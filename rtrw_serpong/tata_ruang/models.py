from common.models import BaseModel
from djgeojson.fields import PolygonField
from django.db import models


class BidangTanah(BaseModel):
    tipe_bidang_tanah = models.ForeignKey('master.TipeBidangTanah',
                                          on_delete=models.PROTECT)
    pemilik = models.ForeignKey('kependudukan.Biodata', null=True, blank=True,
                                on_delete=models.PROTECT)
    deskripsi = models.TextField()
    picture = models.ImageField(null=True, blank=True)
    geom = PolygonField()
    induk = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT,
                              help_text="Bidang tanah induk yang mencakupi")

    class Meta:
        verbose_name = 'Bidang Tanah'
        verbose_name_plural = 'Bidang Tanah'

    def __str__(self) -> str:
        return f"{self.deskripsi} ({str(self.pk)})"

    @property
    def picture_url(self):
        return self.picture.url


class Bangunan(BaseModel):
    bidang_tanah = models.ForeignKey(
        BidangTanah, on_delete=models.PROTECT, null=True, blank=True)
    pemilik = models.ForeignKey('kependudukan.Biodata', null=True, blank=True,
                                on_delete=models.PROTECT)
    alamat = models.CharField(max_length=255)
    geom = PolygonField(null=True)
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


class Ruangan(BaseModel):
    bangunan = models.ForeignKey(Bangunan, null=True, blank=True,
                                 on_delete=models.PROTECT)
    nomor = models.CharField(max_length=3, blank=True, null=True)
    disewakan = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Ruangan'
        verbose_name_plural = 'Ruangan'
        unique_together = ('bangunan', 'nomor', )

    def __str__(self) -> str:
        if self.nomor:
            return f"{self.bangunan}:{str(self.nomor)}"
        else:
            return f"{self.bangunan}:{str(self.pk)}"
