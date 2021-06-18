# Dokumentasi

## Instalasi

### GDAL Library

https://docs.djangoproject.com/en/3.2/ref/contrib/gis/install/

Berikut adalah petunjuk instalasi library geospatial untuk OS Debian/Ubuntu:
```sh
sudo apt-get install binutils libproj-dev gdal-bin
```

### Inisialisasi Data
Kita melakukan inisialisasi data menggunakan `fixtures`.

#### Data Master
```bash
python manage.py loaddata master/fixtures/*
```

## Menjalankan Webserver

Webserver Django dijalankan menggunakan command berikut.
```bash
python manage.py runserver
```

Buka browser anda di http://localhost:8000

## Deploy Menggunakan Docker

```bash
cd docker
docker-compose -f docker-compose.yml up -d
```

## Catatan

### Credentials di S3
#### Upload
```bash
aws s3 cp docker/.env s3://rtrw-serpong/dev/docker/.env \
&& aws s3 cp rtrw_serpong/.env s3://rtrw-serpong/dev/rtrw_serpong/.env \
&& aws s3 cp rtrw_serpong/allauth_socialaccount.json s3://rtrw-serpong/dev/rtrw_serpong/allauth_socialaccount.json
```

#### Download
```bash
aws s3 cp s3://rtrw-serpong/dev/docker/.env docker/.env \
&& aws s3 cp s3://rtrw-serpong/dev/rtrw_serpong/.env rtrw_serpong/.env \
&& aws s3 cp s3://rtrw-serpong/dev/rtrw_serpong/allauth_socialaccount.json rtrw_serpong/allauth_socialaccount.json
```

### Memperbarui Static File
```bash
python manage.py collectstatic --noinput --clear
```

### Dump Social App
Kita bisa menyimpan keluar data social app dengan cara berikut:
```bash
python manage.py dumpdata socialaccount > allauth_socialaccount.json
```

Sehingga, kita bisa menggunakannya untuk load sebagai fixture:
```bash
python manage.py loaddata allauth_socialaccount.json

# atau dengan Docker
docker exec -it django python manage.py loaddata allauth_socialaccount.json
```

### Mencetak Ulang File Migrasi
Bersihkan semua direktori migrasi:
```bash
rm -rf db.sqlite3 master/migrations/ kependudukan/migrations/ tata_ruang/migrations/ home/migrations/
```

Membuat ulang migrasi
```bash
python manage.py makemigrations master kependudukan tata_ruang home
python manage.py migrate
```