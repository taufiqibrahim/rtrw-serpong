# Generated by Django 3.2.4 on 2021-06-16 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Data Dibuat')),
                ('created_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Dibuat Oleh')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Tanggal Data Diperbarui')),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Diperbarui Oleh')),
                ('nik', models.CharField(max_length=16, unique=True, verbose_name='NIK')),
                ('no_paspor', models.CharField(blank=True, max_length=90, null=True)),
                ('nama_lengkap', models.CharField(max_length=180)),
                ('tempat_lahir', models.CharField(max_length=180)),
                ('tanggal_lahir', models.DateField()),
                ('no_akta_lahir', models.CharField(blank=True, max_length=120, null=True)),
                ('no_akta_kawin', models.CharField(blank=True, max_length=120, null=True)),
                ('tanggal_kawin', models.DateField(blank=True, null=True)),
                ('no_akta_cerai', models.CharField(blank=True, max_length=120, null=True)),
                ('tanggal_cerai', models.DateField(blank=True, null=True)),
                ('nik_ibu', models.CharField(max_length=16, verbose_name='NIK ibu')),
                ('nama_lengkap_ibu', models.CharField(max_length=180)),
                ('nik_ayah', models.CharField(max_length=16, verbose_name='NIK ayah')),
                ('nama_lengkap_ayah', models.CharField(max_length=180)),
                ('nama_ketua_rt', models.CharField(blank=True, max_length=180, null=True, verbose_name='Nama ketua RT')),
                ('nama_ketua_rw', models.CharField(blank=True, max_length=180, null=True, verbose_name='Nama ketua RW')),
            ],
            options={
                'verbose_name': 'Biodata',
                'verbose_name_plural': 'Biodata',
            },
        ),
        migrations.CreateModel(
            name='Keluarga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Data Dibuat')),
                ('created_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Dibuat Oleh')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Tanggal Data Diperbarui')),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Diperbarui Oleh')),
                ('no_kk', models.CharField(max_length=16, unique=True, verbose_name='No KK')),
                ('nama_kepala', models.CharField(max_length=180)),
                ('alamat', models.CharField(max_length=360)),
            ],
            options={
                'verbose_name': 'Keluarga',
                'verbose_name_plural': 'Keluarga',
            },
        ),
        migrations.CreateModel(
            name='Domisili',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Tanggal Data Dibuat')),
                ('created_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Dibuat Oleh')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Tanggal Data Diperbarui')),
                ('updated_by', models.CharField(blank=True, max_length=50, null=True, verbose_name='Data Diperbarui Oleh')),
                ('tanggal_mulai_tinggal', models.DateField()),
                ('tanggal_akhir_tinggal', models.DateField(blank=True, default=None, null=True)),
                ('biodata', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='kependudukan.biodata')),
            ],
            options={
                'verbose_name': 'Domisili',
                'verbose_name_plural': 'Domisili',
            },
        ),
    ]
