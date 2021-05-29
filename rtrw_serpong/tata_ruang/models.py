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
