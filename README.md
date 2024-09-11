# disco-paradise

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**JAWAB**
- Melakukan setup awal seperti menentukan nama, tema proyek dan pembuatan direktori dari proyek tersebut. Lalu install django dan membuat virtual environment. Lakukan pengecekan terhadap virtual environment jika ada masalah.
- Buat requirements.txt yang berisi dengan segala macam dependencies yang akan digunakan dalam proyek django yang akan dibuat. 
- membuat direktori proyek dengan menggunakan perintah django-admin startproject discoparadise . yang akan jadi direktori aplikasi saya.
- Membuat direktori baru bernama main dengan menggunakan perintah python manage.py startapp main . yang akan menjadi bagian utama untuk konfigurasi aplikasi saya
- Dengan terinisialisasinya main, saya lanjut membuat model dari aplikasi saya yang akan berlangsung pada models.py pada direktori main

Atribut yang saya gunakan untuk proyek saya:

from django.db import models

class AlbumEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    date_of_distribution = models.TextField()
    stock_available = models.IntegerField()
    genre = models.TextField()

- Setelah saya membuat model tersebut, saya melakukan imigrasi model ke basis data lokal.
- Buat folder baru di dalam direktori main bernama templates, dimana di dalam direktori ini akan diisi dengan file html bernama main.html yang akan menampilkan segala macam models yang saya buat tadi.
- Hubungkan template dengan views dengan pertama membuat fungsi show_main dalam file views.py seperti berikut: 

from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Dark Side of the Moon',
        'price' : '650000',
        'description' : 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd',
        'date_of_distribution' : '1 March 1973',
        'stock_available' : 10,
        'genre' : 'rock'
    }

    return render(request, "main.html", context)

- Buatkan routing URL aplikasi main dengan mengisi urls.py dalam direktori templates sebagai berikut:

from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]

- Setelah membuat routing URL aplikasi main, saya membuat routing pada proyek agar dapat dijalankan. Caranya adalah untuk mengisi file urls.py dalam direktori disco_paradise sebagai berikut:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
***SAVE FOR LATER***

3. Jelaskan fungsi git dalam pengembangan perangkat lunak
**JAWAB**
Git memiliki beberapa fungsi untuk pengembangan perangkat lunak, beberapa dari fungsi tersebut adalah:
1. Version Control: Git melacak setiap perubahan kode, sehingga developer dapat melihat riwayat versi dan bahkan beralih kepada versi sebelumnya jika ada kesalahan. Hal tersebut mungkin karena command fitur, reset dan checkout dalam git.
2. Collaboration: Git membuka cara untuk melakukan kolaborasi antar developer yang mengerjakan suatu proyek bersama dengan adanya fitur branching dan merging.
3. Deployment: Git memungkinkan developer untuk melakukan deployment ke production server secara mudah dengan adanya command push untuk mengirim versi terbaru dari repositori lokal ataupun pull untuk menerima versi terbaru dari server git.

4. 

5. Mengapa model pada Django disebut sebagai ORM?
**JAWAB**
Model pada Django disebut ORM karena mereka berfungsi untuk menghubungkan objek-objek dalam kode Python dengan tabel-tabel pada database relasional, seperti SQL. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek Python tanpa harus menulis perintah SQL secara langsung.