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


## Catatan

### Memperbarui Static File
```bash
python manage.py collectstatic --noinput --clear
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