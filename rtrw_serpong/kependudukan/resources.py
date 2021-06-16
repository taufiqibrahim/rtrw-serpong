from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import Biodata, Keluarga
from master.models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin, Pendidikan, Pekerjaan, StatusKawin


class KeluargaResource(resources.ModelResource):

    class Meta:
        model = Keluarga
        import_id_fields = ('no_kk',)
        fields = (
            'no_kk',
            'nama_kepala',
            'alamat',
        )
        export_order = fields


class BiodataResource(resources.ModelResource):

    jenis_kelamin = fields.Field(column_name='jenis_kelamin', attribute='jenis_kelamin',
                                 widget=ForeignKeyWidget(JenisKelamin, 'nama'))
    golongan_darah = fields.Field(column_name='golongan_darah', attribute='golongan_darah',
                                  widget=ForeignKeyWidget(GolonganDarah, 'nama'))
    agama = fields.Field(column_name='agama', attribute='agama',
                         widget=ForeignKeyWidget(Agama, 'id'))
    status_kawin = fields.Field(column_name='status_kawin', attribute='status_kawin',
                                widget=ForeignKeyWidget(StatusKawin, 'nama'))
    stat_hubungan_keluarga = fields.Field(column_name='stat_hubungan_keluarga', attribute='stat_hubungan_keluarga',
                                          widget=ForeignKeyWidget(HubunganKeluarga, 'nama'))
    pendidikan_akhir = fields.Field(column_name='pendidikan_akhir', attribute='pendidikan_akhir',
                                    widget=ForeignKeyWidget(Pendidikan, 'nama'))
    jenis_pekerjaan = fields.Field(column_name='jenis_pekerjaan', attribute='jenis_pekerjaan',
                                   widget=ForeignKeyWidget(Pekerjaan, 'nama'))
    keluarga = fields.Field(column_name='no_kk', attribute='keluarga',
                            widget=ForeignKeyWidget(Keluarga, 'no_kk'))

    class Meta:
        model = Biodata
        import_id_fields = ('nik',)
        fields = (
            'nik',
            'no_paspor',
            'nama_lengkap',
            'jenis_kelamin',
            'tempat_lahir',
            'tanggal_lahir',
            'no_akta_lahir',
            'golongan_darah',
            'agama',
            'status_kawin',
            'no_akta_kawin',
            'tanggal_kawin',
            'no_akta_cerai',
            'tanggal_cerai',
            'stat_hubungan_keluarga',
            'pendidikan_akhir',
            'jenis_pekerjaan',
            'nik_ibu',
            'nama_lengkap_ibu',
            'nik_ayah',
            'nama_lengkap_ayah',
            'nama_ketua_rt',
            'nama_ketua_rw',
            'keluarga',
        )
        export_order = fields
