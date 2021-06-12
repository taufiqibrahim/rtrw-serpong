from django.db import models
from common.models import BaseModel
from master.models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin, Pendidikan, Pekerjaan, StatusKawin


class Keluarga(BaseModel):
    no_kk = models.CharField(verbose_name='No KK', max_length=16, null=False,
                             blank=False, unique=True)
    # file_kk = models.FieldFile(upload_to='file_kk')
    nama_kepala = models.CharField(max_length=180)
    alamat = models.CharField(max_length=360)
    # NO_RT             NUMBER(3),
    # NO_RW             NUMBER(3),
    # DUSUN             VARCHAR2(180 BYTE),
    # KODE_POS          NUMBER(5),
    # TELP              VARCHAR2(90 BYTE),
    # ALS_PRMOHON       NUMBER(1),
    # ALS_NUMPANG       NUMBER(1),
    # NO_PROP           NUMBER(2),
    # NO_KAB            NUMBER(2),
    # NO_KEC            NUMBER(2),
    # NO_KEL            NUMBER(4),
    # USERID            NUMBER,
    # TGL_INSERTION     DATE,
    # TGL_UPDATION      DATE,
    # PFLAG             VARCHAR2(3 BYTE),
    # CFLAG             VARCHAR2(3 BYTE),
    # SYNC_FLAG         NUMBER(1),
    # OA_NAMA_PERTAMA   VARCHAR2(180 BYTE),
    # OA_NAMA_KELUARGA  VARCHAR2(180 BYTE),
    # TIPE_KK           VARCHAR2(14 BYTE),
    # NIK_KK            NUMBER(16),
    # COUNT_KK          NUMBER,
    # TGL_REPLIKASI     DATE,
    # DATA_STATUS       NUMBER

    class Meta:
        verbose_name = 'Keluarga'
        verbose_name_plural = 'Keluarga'

    def __str__(self) -> str:
        return self.no_kk


class Biodata(BaseModel):
    nik = models.CharField(verbose_name='NIK', max_length=16,
                           null=False, blank=False, unique=True)
    # file_ktp = models.FieldFile(upload_to='file_ktp')
    # NO_KTP            VARCHAR2(120 BYTE),
    # TMPT_SBL          VARCHAR2(900 BYTE),
    no_paspor = models.CharField(max_length=90, null=True, blank=True)
    # TGL_AKH_PASPOR    DATE,
    nama_lengkap = models.CharField(max_length=180)
    jenis_kelamin = models.ForeignKey(JenisKelamin, on_delete=models.PROTECT)
    tempat_lahir = models.CharField(max_length=180)
    tanggal_lahir = models.DateField()
    # AKTA_LHR          NUMBER(1),
    no_akta_lahir = models.CharField(max_length=120, null=True, blank=True)
    golongan_darah = models.ForeignKey(GolonganDarah, on_delete=models.PROTECT)
    agama = models.ForeignKey('master.Agama', on_delete=models.PROTECT)
    status_kawin = models.ForeignKey(StatusKawin, on_delete=models.PROTECT)
    # AKTA_KWN          NUMBER(1),
    no_akta_kawin = models.CharField(max_length=120, null=True, blank=True)
    tanggal_kawin = models.DateField(null=True, blank=True)
    # AKTA_CRAI         NUMBER(1),
    no_akta_cerai = models.CharField(max_length=120, null=True, blank=True)
    tanggal_cerai = models.DateField(null=True, blank=True)
    stat_hubungan_keluarga = models.ForeignKey(
        HubunganKeluarga, on_delete=models.PROTECT)
    # KLAIN_FSK         NUMBER(1),
    # PNYDNG_CCT        NUMBER(1),
    pendidikan_akhir = models.ForeignKey(Pendidikan, on_delete=models.PROTECT)
    jenis_pekerjaan = models.ForeignKey(Pekerjaan, on_delete=models.PROTECT)
    nik_ibu = models.CharField(
        verbose_name='NIK ibu', max_length=16, null=False, blank=False)
    nama_lengkap_ibu = models.CharField(max_length=180)
    nik_ayah = models.CharField(
        verbose_name='NIK ayah', max_length=16, null=False, blank=False)
    nama_lengkap_ayah = models.CharField(max_length=180)
    nama_ketua_rt = models.CharField(
        verbose_name='Nama ketua RT', max_length=180, null=True, blank=True)
    nama_ketua_rw = models.CharField(
        verbose_name='Nama ketua RW', max_length=180, null=True, blank=True)
    # NAMA_PET_REG      VARCHAR2(180 BYTE),
    # NIP_PET_REG       NUMBER,
    # NAMA_PET_ENTRI    VARCHAR2(180 BYTE),
    # NIP_PET_ENTRI     NUMBER,
    # TGL_ENTRI         DATE,
    keluarga = models.ForeignKey(
        Keluarga, on_delete=models.PROTECT, verbose_name='No KK')
    # no_kk = models.CharField(verbose_name='No KK',
    #                          max_length=16, null=True, blank=True, )
    # JENIS_BNTU        NUMBER(2),
    # NO_PROP           NUMBER(2),
    # NO_KAB            NUMBER(2),
    # NO_KEC            NUMBER(2),
    # NO_KEL            NUMBER(4),
    # STAT_HIDUP        NUMBER(10),
    # TGL_UBAH          DATE,
    # TGL_CETAK_KTP     DATE,
    # TGL_GANTI_KTP     DATE,
    # TGL_PJG_KTP       DATE,
    # STAT_KTP          NUMBER(1),
    # ALS_NUMPANG       NUMBER(1),
    # PFLAG             VARCHAR2(3 BYTE),
    # CFLAG             VARCHAR2(3 BYTE),
    # SYNC_FLAG         NUMBER(1),
    # KET_AGAMA         VARCHAR2(180 BYTE),
    # KEBANGSAAN        VARCHAR2(180 BYTE),
    # GELAR             VARCHAR2(36 BYTE),
    # KET_PKRJN         VARCHAR2(180 BYTE),
    # GLR_AGAMA         VARCHAR2(3 BYTE),
    # GLR_AKADEMIS      VARCHAR2(3 BYTE),
    # GLR_BANGSAWAN     VARCHAR2(3 BYTE),
    # IS_PROS_DATANG    VARCHAR2(3 BYTE),
    # DESC_PEKERJAAN    VARCHAR2(90 BYTE),
    # DESC_KEPERCAYAAN  VARCHAR2(90 BYTE),
    # FLAG_STATUS       VARCHAR2(3 BYTE),
    # COUNT_KTP         NUMBER,
    # COUNT_BIODATA     NUMBER,
    # TGL_REPLIKASI     DATE,
    # DATA_STATUS       NUMBER,
    # DKB_SEMESTER      NUMBER

    class Meta:
        verbose_name = 'Biodata'
        verbose_name_plural = 'Biodata'

    def __str__(self) -> str:
        return self.nik
