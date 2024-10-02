# disco-paradise
## TUGAS 2
## [Visit Disco Paradise here!](https://refalino-shahzada-discoparadisee.pbp.cs.ui.ac.id/)

### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**JAWAB**
- Melakukan setup awal seperti menentukan nama, tema proyek dan pembuatan direktori dari proyek tersebut. Lalu install django dan membuat virtual environment. Lakukan pengecekan terhadap virtual environment jika ada masalah.
- Buat requirements.txt yang berisi dengan segala macam dependencies yang akan digunakan dalam proyek django yang akan dibuat. 
- membuat direktori proyek dengan menggunakan perintah django-admin startproject discoparadise . yang akan jadi direktori aplikasi saya.
- Membuat direktori baru bernama main dengan menggunakan perintah python manage.py startapp main . yang akan menjadi bagian utama untuk konfigurasi aplikasi saya
- Dengan terinisialisasinya main, saya lanjut membuat model dari aplikasi saya yang akan berlangsung pada models.py pada direktori main. Atribut yang saya gunakan untuk proyek saya:
```python
from django.db import models

class AlbumEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    date_of_distribution = models.TextField()
    stock_available = models.IntegerField()
    genre = models.TextField()
```
- Setelah saya membuat model tersebut, saya melakukan imigrasi model ke basis data lokal.
- Buat folder baru di dalam direktori main bernama templates, dimana di dalam direktori ini akan diisi dengan file html bernama main.html yang akan menampilkan segala macam models yang saya buat tadi.
- Hubungkan template dengan views dengan pertama membuat fungsi show_main dalam file views.py seperti berikut: 
```python
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
```
- Buatkan routing URL aplikasi main dengan mengisi urls.py dalam direktori templates sebagai berikut:
```python
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
- Setelah membuat routing URL aplikasi main, saya membuat routing pada proyek agar dapat dijalankan. Caranya adalah untuk mengisi file urls.py dalam direktori disco_paradise sebagai berikut:
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
***JAWAB***
![Diagram Django Keren](DiagramDjango.png)
- Client mengirim request ke server
- urls.py melakukan URL routing yang menangkap request dan mengarahkan ke view yang sesuai 
- views.py memoproses request tersebut, berinteraksi dengan model dan mengembalikan response
- models.py berisi dengan model yang berinteraksi dengan database untuk mengambil dan menyimpan data
- HTML Template merupakan hasil view yang di render dengan data yang diperoleh dari model dan mengembalikan response ke client.

### 3. Jelaskan fungsi git dalam pengembangan perangkat lunak
**JAWAB**
Git memiliki beberapa fungsi untuk pengembangan perangkat lunak, beberapa dari fungsi tersebut adalah:
- Version Control: Git melacak setiap perubahan kode, sehingga developer dapat melihat riwayat versi dan bahkan beralih kepada versi sebelumnya jika ada kesalahan. Hal tersebut mungkin karena command fitur, reset dan checkout dalam git.
- Collaboration: Git membuka cara untuk melakukan kolaborasi antar developer yang mengerjakan suatu proyek bersama dengan adanya fitur branching dan merging.
- Deployment: Git memungkinkan developer untuk melakukan deployment ke production server secara mudah dengan adanya command push untuk mengirim versi terbaru dari repositori lokal ataupun pull untuk menerima versi terbaru dari server git.

### 4. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
***JAWAB*** 
Django dijadikan permulaan pembelajaran pengembangan perangkat lunak karena alasan sebagai berikut:
- Django sudah menyediakan banyak fitur bawaan untuk pengembangan aplikasi web
- Django dirancang utuk menangani aplikasi yang kompleks
- Django sudah menyediakan fitur berupa keamanan yang melindungi aplikasi dari ancaman
- Django memiliki komunitas yang besar hingga dapat saling tanya dan belajar

### 5. Mengapa model pada Django disebut sebagai ORM?
**JAWAB**
Model pada Django disebut ORM karena mereka berfungsi untuk menghubungkan objek-objek dalam kode Python dengan tabel-tabel pada database relasional, seperti SQL. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek Python tanpa harus menulis perintah SQL secara langsung.

## TUGAS 3

### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
**JAWAB**
Data delivery sangat penting untuk diimplementasikan dalam sebuah platform karena beberapa hal berikut:
- Data delivery menyediakan akses langsung kepada real-time information dimana kita sebuah platform akan dapat data dan informasi terbaru.
- Dengan adanya data delivery dan real time information yang masuk, terdapat user engagement yang lebih menarik karena rekomendasi yang sesuai dengan data yang diambil dari user.
- Dengan adanya data delivery, developer akan lebih mudah untuk menentukan gerakan kedepannya dengan segala input dan data dari user.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
**JAWAB**
Menurut saya, JSON lebih baik dibandingkan dengan XML. Alasannya juga sama dengan mengapa JSON lebih popular dibandingkan dengan XML. 
- JSON memiliki syntax yang jauh lebih simple untuk dibaca. 
- JSON memiliki format data yang lebih kecil, sehingga penguraian data lebih cepat
- JSON sudah menjadi format standar untuk mayoritas service web dan API

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
**JAWAB**
`is_valid()` adalah fungsi di dalam Django yang digunakan untuk validasi. Mayoritas fungsi `is_valid()` pada django digunakan pada forms dan model dimana dia berfungsi untuk ngecek apabila suatu data sudah valid sebelum di proses dan di simpan. 

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
**JAWAB**
Pertama harus diketahui bahwa CSRF adalah Cross-Site Request Forgery dan csrf token adalah suatu token unik yang dibuat oleh server untukk memastikan bahwa suatu request yang sedang diproses itu aman dan diautentikasi. Jika tidak menggunakan `csrf_token`, dapat terjadi kejahatan-kejahatan seperti tindakan dari pihak asing, masalah integritas data dan ketidakamanan.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**JAWAB**
***Membuat input form untuk menambahkan objek model pada app sebelumnya.***
1. Untuk menambah input form, saya pertama membuat berkas baru pada direktori `main` dengan nama `forms.py` dan saya isi dengan kode berikut:
```python
from django.forms import ModelForm
from main.models import AlbumEntry

class AlbumEntryForm(ModelForm):
    class Meta:
        model = AlbumEntry
        fields = ["name", "price", "description", "date_of_distribution", "stock_available", "genre"]
```
Penjelasan:
- `model = AlbumEntry` berfungsi untuk menunjukkan model yang akan digunakan untuk form.
- `fields = ["name", "price", "description", "date_of_distribution", "stock_available", "genre"]` berfungsi untuk menunjukkan fields yang akan diisi oleh form AlbumEntry

2. Lalu pada berkas `views.py` pada direktori `main` import `AlbumEntry` dan `AlbumEntryForms` dan membuat function baru bernama `create_album_entry` sebagai berikut:
```python
def create_album_entry(request):
    form = AlbumEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    context = {'form': form}
    return render(request, "create_album_entry.html", context)
```
Penjelasan:
- `form = AlbumEntryForm(request.POST or None)` digunakan untuk membuat entry form baru dengan memasukkan *QueryDict* berdasarkan input *user* pada `request.POST`
- `form.is_valid()` digunakan untuk validasi isi input form tersebut
- `form.save()` digunakan untuk menyimpan data dari form tersebut
- `return redirect("main:show_main")` digunakan untuk melakukan *redirect* ke fungsi `show_main` pada views aplikasi `main` setelah data form berhasil disimpan.

3. Dari tugas sebelumnya, saya mengubah fungsi `show_main` menjadi seperti berikut:
```python
def show_main(request):
    album_entries = AlbumEntry.objects.all()

    context = {
        'name': 'Dark Side of the Moon',
        'price' : '650000',
        'description' : 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd',
        'date_of_distribution' : '1 March 1973',
        'stock_available' : 10,
        'genre' : 'rock',
        'album_entries': album_entries,
    }

    return render(request, "main.html", context)
```
Penjelasan:
- `AlbumEntry.objects.all()` yang dimasukkan kedalam variabel album_entries merupakan seluruh objek AlbumEntry yang disimpan pada database. 

4. Pada direktori `main`, buka berkas `urls.py` saya import fungsi `create_album_entry` yang saya buat dan tambahkan variabel baru pada urlpatterns untuk mengakses fungsi yang diimport seperti berikut:
```python
urlpatterns = [
   ...
   path('create-album-entry', create_album_entry, name='create_album_entry'),
]
```
5. Pada subdirektori `templates` di dalam direktori `main` saya buat berkas baru bernama `create_album_entry.html` yang berisi dengan kode berikut:
```html
{% extends 'base.html' %} 
{% block content %}
<h1>Add New Album Entry</h1>

<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td>
        <input type="submit" value="Add Album Entry" />
      </td>
    </tr>
  </table>
</form>

{% endblock %}
```
Penjelasan:
- `form method="POST"` digunakan untuk menandakan block untuk form metode POST
- `{% csrf_token %}` adalah token yang berfungsi sebagai security dalam rangka html tersebut untuk mencegah serangan berbahaya.
- `{{ form.as_table }}` adalah template tag yang digunakan untuk menampilkan fields form yang sudah dibuat pada `forms.py` sebagai table.
- `<input type="submit" value="Add Album Entry" />` digunakan sebagai tombol untuk menyimpan data yang sudah diisi dalam form 

6. Pada direktori sama, pada `main.html` tambahkan {% block content %} untuk menampilkan data album dalam bentuk tabel dan tombol "Add New Album Entry" yang akan lakukan redirect ke halaman mengisi form sebagai berikut:
```html
{% if not album_entries %}
<p>Belum ada data album pada Disco Paradise.</p>
{% else %}
<table>
  <tr>
    <th>Album Name</th>
    <th>Price</th>
    <th>Description</th>
    <th>Date of Distribution</th>
    <th>Stock Available</th>
    <th>Genre</th>
  </tr>

  {% comment %} Berikut cara memperlihatkan data album di bawah baris ini 
  {% endcomment %} 
  {% for album_entry in album_entries %}
  <tr>
    <td>{{album_entry.name}}</td>
    <td>{{album_entry.price}}</td>
    <td>{{album_entry.description}}</td>
    <td>{{album_entry.date_of_distribution}}</td>
    <td>{{album_entry.stock_available}}</td>
    <td>{{album_entry.genre}}</td>
  </tr>
  {% endfor %}
</table>
{% endif %}

<br />

<a href="{% url 'main:create_album_entry' %}">
  <button>Add New Album Entry</button>
</a>
{% endblock content %}
```
Dengan itu, pembuatan form untuk menambahkan objek model sudah selesai.

***Tambahkan 4 fungsi `views` baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.***
1. Pada direktori `main` buka berkas `views.py` dan import `HttpResponse` dan `serializers` sebagai berikut:
```python
from django.http import HttpResponse
from django.core import serializers
```

2. Untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by id dan JSON by id buatlah fungsi baru untuk masing-masing keperluan sebagai berikut:
**UNTUK XML**
```python 
def show_xml(request):
    data = AlbumEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
**UNTUK JSON**
```python
def show_json(request):
    data = AlbumEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

**UNTUK XML by id**
```python
def show_xml_by_id(request, id):
    data = AlbumEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```

**UNTUK JSON by id***
```python
def show_json_by_id(request, id):
    data = AlbumEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

3. Lalu pada berkas `urls.py` pada direktori `main` import semua fungsi tersebut serta tambahkan path url untuk mengakses masing-masing fungsi seperti berikut:

### 6. Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam `README.md`.

Pada XML:
![Show XML](show_xml.jpg)

Pada JSON:
![Show JSON](show_json.jpg)

Pada XML by ID:
![Show JSON by ID](show_xml_by_id.jpg)

Pada JSON by ID:
![Show JSON by ID](show_json_by_id.jpg)

## TUGAS 4
### 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
UserCreation form pada django merupakan sistem autentikasi yang dibuat langsung di dalam frameworknya. Fungsinya untuk membuat user baru dengan menggunakan username, password dan password confirmation.

***Kelebihan:**
- UserCreationForm merupakan bawaan dari Django hingga mudah untuk diakses dan digunakan
- Kemanan sistem yang sangat baik karena password hashing
- Form autentikasinya dapat disesuaikan dengan kemauan user

**Kekurangan:**
- Hanya memiliki form username dan password, jika ingin lebih banyak form harus di extend
- Form default tidak memiliki UX yang baik, kekurangan indikator kekuatan password dan sebagainya.
- Biarpun form dapat di extend untuk memiliki lebih banyak field, tetap sulit dan membutuhkan pemahaman Django yang cukup banyak

### 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi dan otorisasi adalah 2 konsep berbeda namun saling terkait dan keduanya sangat penting dalam menjaga keamanan aplikasi. 

**Autentikasi**
Autentikasi adalah proses memverifikasi identitas pengguna. Dalam kata lain menentukan siapa yang masuk ke sistem. Sebagai contoh dari proses autentikasi adalah ketika pengguna masukkan username dan password pada halaman login, Django menggunakan sistem autentikasi bawaan untuk memverifikasi apakah kredensial tersebut cocok dengan data yang disimpan pada database.

**Otorisasi**
Otorisasi adalah proses untuk menentukan apa yang bisa dilakukan oleh pengguna yang telah diautentikasi. Otorisasi menentukan izin dan hak akses yang dimiliki oleh pengguna. Sebagai contoh dari proses otorisasi adalah ketika pengguna masuk ke akun mereka, otorisasi memeriksa apakah pengguna tersebut memiliki izin untuk mengakses halaman admin, mengedit data, menghapus konten. 

**Mengapa keduanya penting**
Ada beberapa alasan mengapa kedua hal tersebut penting, beberapa dari hal tersebut adalah:
- Keamanan aplikasi: Autentikasi memastikan hanya pengguna yang sah yang dapat masuk ke dalam sistem dan otorisasi akan memastikan bahwa pengguna tersebut hanya bisa mengakses bagian yang diizinkan kepada mereka.
- Privasi dan hak akses: Otorisasi menjaga agar pengguna hanya bisa mengakses data dan fitur yang relevan dengan peran atau izin mereka. 
- User experience: Dengan memisahkan autentikasi dan otorisasi, aplikasi dapat memberikan user experience yang lebih aman dan terstruktur.

### 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
**Apa itu cookies dalam konteks aplikasi web?**
Cookies adalah file kecil yang disimpan oleh browser di perangkat pengguna ketika mereka mengunjungi situs web. Cookies digunakan untuk menyimpan data kecil yang bisa dikirim kembali ke server setiap kali pengguna membuat permintaan baru. Cookies membantu aplikasi web untuk mengingat pengguna atau informasi tentang sesi mereka saat berpindah-pindah antara halaman atau ketika kembali ke situs di lain waktu.

**Bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?**
Django menggunakan cookies untuk mengelola sesi pengguna, sehingga situs web dapat mengingat pengguna di antara permintaan HTTP. Sebagai contoh, dengan sistem sesi Django, pengguna dapat memiliki preferensi terhadap sesuatu yang diingat dan tidak harus dikirim ulang di setiap halaman. Untuk bagaimana cara kerjanya sebagai berikut:
  1. Ketika pengguna pertama kali mengunjungi aplikasi Django, cookie `sessionid` disimpan di browser mereka, cookie ini berisi dengan ID sesi unik yang dihasilkan secara acak.
  2. Django menyimpan data sesi pengguna di server. Data yang disimpan bisa berupa status login atau informasi sementara lainnya. ID sesi yang disimpan ini memungkinkan Django untuk mengambil dan menggunakan data sesi ketika pengguna mengirim permintaan baru.
  3. Setiap kali pengguna mengirim permintaan HTTP, Django membaca cookie `sessionid` dari broser tersebut. Jika cocok, Django akan mengembalikan data sesi yang terkait dengan pengguna tersebut. Jika sesi pengguna berakhir atau logout, Django akan menghapus data sesi di server dan cookie `sessionid`.
  4. Django menggunakan cookies untuk keamanan, dengan menerapkan token CSRF untuk mencegah serangan Cross-Site Request Forgery. Ini melibatkan penyimpenan token CSRF di cookie, yang kemudian diverifikasi setiap kali pengguna mengirimkan permintaan POST.

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan cookies dalam pengembangan web tidak sepenuhnya aman secara default. Ada beberapa risiko yang harus diwaspadai, terutama karena cookies dapat digunakan untuk menyimpan data sensitif. Beberapa risiko potensial dalam penggunaan cookies adalah:
- XSS atau Serangan Cross-Site Scripting dimana penyerang mengimplementasikan sebuah skrip berbahaya ke dalam aplikasi web yang dapat mengambil data sesi pengguna sebuah pengguna
- Serangan CSRF atau Cross-Site Request Forgery adalah serangan di mana penyerang mencoba membuat pengguna yang sudah terautentikasi mengirimkan permintaan yang tidak sah kepada server tanpa sepengetahuan mereka. 
- Serangan cookie theft terjadi ketika penyerang mencuri cookie dari pengguna, biasanya melalui jaringan yang tidak aman seperti Wi-Fi publik.

### 5.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
**Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.**
  1. Membuat fungsi dan form registrasi
  Pada file `views.py` saya import `UserCreationForm` dan `messages`. Kemudian saya tambahkan fungsi `register` pada file yang sama seperti berikut:
  ```python
  def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
  ```
  Dimana fungsi ini akan menghasilkan form registrasi secara otomatis dan akan menghasilkan akun pengguna ketika di submit dari form. Setelah itu, saya membuat kerangka halaman registrasi dengan membuat file html baru bernama `register.html` dengan isi berikut:
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}

  {% block content %}

  <div class="login">
    <h1>Register</h1>

    <form method="POST">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input type="submit" name="submit" value="Daftar" /></td>
        </tr>
      </table>
    </form>

    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </div>

  {% endblock content %}
  ```
  Html tersebut yang akan menjadi kerangka dari halaman register saya. Kemudian saya hubungkan form register serta kerangkanya dengan url tertentu dengan membuka `urls.py` dan menambahkan path untuk register.

  2. Membuat fungsi dan form login
  Sebelum mulai, saya import `Authenticate`, `login`, dan `AuthenticationForm` pada berkas `views.py` kemudian menambahkan fungsi `login_user` pada berkas yang sama seperti berikut:
  ```python
  def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main:show_main')

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
   ```
  Setelah saya membuat fungsi login, saya membuat kerangka yang akan di display di website dengan file html baru bernama `login.html` yang berisi sebagai berikut:\
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
      {% csrf_token %}
      <table>
        {{ form.as_table }}
        <tr>
          <td></td>
          <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
      </table>
    </form>

    {% if messages %}
    <ul>
      {% for message in messages %}
      <li>{{ message }}</li>
      {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
  </div>

  {% endblock content %}
  ```
  Kemudian saya routing kerangka dan fungsi tersebut dengan import fungsi `login_user` dan menambahkan path url baru pada `urlpatterns`

  3. Membuat fungsi logout
  Pada `views.py`, saya import `logout` dan menambahkan fungsi `logout_user` yang berfungsi sebagai mekanisme logout seperti berikut:
  ```python
  def logout_user(request):
    logout(request)
    return redirect('main:login')
  ```
  Kemudian pada berkas `main.html` saya tambahkan button logout seperti berikut:
  ```html
  <a href="{% url 'main:logout' %}">
    <button>Logout</button>
  </a>
  ```
  Kemudian pada `urls.py` saya import fungsi `logout_user` dan tambahkan url path baru pada `urlpatterns` dengan url baru untuk logout.

  4. Merestriksi Akses Halaman Main Sebelum Login
  Pada berkas `views.py` saya import `login_required` dan tambahkan potongan kode `login_required` sebelum fungsi `show_main` seperti berikut:
  ```python
  @login_required(login_url='/login')
  ```

**Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.**
  Dengan implementasinya feature register, login dan logout, untuk membuat dua akun pengguna saya menggunakan feature register saya untuk membuat 2 akun pengguna. Kemudian pada tiap pengguna saya menambahkan album entry sebanyak 3 album.

**Menghubungkan model Product dengan User.**
  1. Pada `models.py` saya import `User` dan ubah variabel user menjadi sebagai berikut:
  ```python
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  ```
  2. Pada `views.py` saya ubah potongan kode pada fungsi `create_album_entry` sebagai berikut:
  ```python
  def create_album_entry(request):
    form = AlbumEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        album_entry = form.save(commit=False)
        album_entry.user = request.user
        album_entry.save()
        return redirect("main:show_main")
    
    context = {'form': form}
    return render(request, "create_album_entry.html", context)
  ```
  3. Saya ubah value pada variabel `album_entries` dan `context` pada fungsi `show_main` seperti berikut:
  ```python
  def show_main(request):
    album_entries = AlbumEntry.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'price' : '650000',
        'description' : 'The Dark Side of the Moon is the eighth studio album by the English rock band Pink Floyd',
        'date_of_distribution' : '1 March 1973',
        'stock_available' : 10,
        'genre' : 'rock',
        'album_entries': album_entries,
        'last_login': request.COOKIES['last_login'],
    }

    return render(request, "main.html", context)
  ```
  4. Lakukan migrasi model pada Django menggunakan `python manage.py makemigrations` dan menetapkan user yang sudah ada dengan ID 1. Kemudian lakukan `python manage.py migrate` untuk mengaplikasikan migrasi yang dilakukan pada poin sebelumnya. Kemudian saya setup aplikasi web kita untuk environment production dengan import `os` pada `settings.py` di subdirektori `disco_paradise` kemudian ganti variabel `DEBUG` seperti berikut:
  ```python
  PRODUCTION = os.getenv("PRODUCTION", False)
  DEBUG = not PRODUCTION
  ```

**Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.**
  1. Pada `views.py` import `HttpResponseRedirect`, `reverse` dan `datetime`
  2. Tambahkan fungsionalitas menambahkan cookie pada fungsi  `login_user` bernama `last_login` dengan menggantikan kode sebagai berikut:
  ```python
  def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
  ```
  Setelah itu, pada fungsi `show_main` saya tambahkan potongan kode `last_login` seperti berikut:
  ```python
  'last_login': request.COOKIES['last_login'],
  ```
  Saya ubah fungsi `logout_user` seperti berikut:
  ```python
  def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
  ```
  3. Tambahkan kerangka pada `main.html` untuk display sesi terakhir login anda.

## TUGAS 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Untuk prioritas pengambilan CSS selector, ada yang namanya CSS Specificity. Dimana jika ada 2 atau lebih selector CSS yang mengarah kepada elemen yang sama, selector yang memiliki specificity paling tinggi akan deklarasikan style untuk element HTML tersebut.

Setiap CSS Selector memiliki tempat pada hirarki specificity. Hirarki specificity dibagi menjadi 4 kategori yaitu:
  1. Inline Styles (`<h1 style="color: pink;">`)
  2. IDS (`#navbar)
  3. Classes, pseudo-classes, attribute selectors (`.test, :hover, [href]`)
  4. Elements and pseudo-elements (`h1, ::before`)
  
Inline Style selalu memiliki specificity paling tinggi, dengan pengecualian ada peraturan `!important` dimana itu akan pasti mengalahkan selector lain.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive Web Design atau RWD adalah salah satu cara dalam web design untuk mengimplementasikan web page yang merender dengan baik pada berbagai macam perangkat berbeda untuk memastikan user experience yang baik. RWD penting dalam pengembangan aplikasi web karena beberapa alasan yaitu:
  1. User experience yang lebih baik
  2. Search Engine Optimization
  3. Penghematan waktu dan biaya
  4. Menjangkau lebih banyak pengguna
  5. Menyesuaikan performa perangkat

- Contoh aplikasi web yang menggunakan RWD adalah Twitter/X
- Contoh aplikasi web yang tidak menggunakan RWD adalah SIAKNG

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Pada CSS, **margin** adalah ruang diluar sebuah border pada suatu element. 
Contoh implementasi margin:
```html
div {
  margin: 20px; /* 20px space around the element outside its border */
}
```
**Border** adalah garis yang mengelilingi padding dan content pada suatu element. Border juga memisahkan padding dengan margin.
Contoh implementasi border:
```html
div {
  border: 2px solid black; /* Black solid border, 2px wide */
}
```
**Padding** adalah ruang yang ada di dalam border suatu element. Padding dapat menambahkan ukuran dari sebuah element tanpa menambahkan ruang diluarnya.
Contoh implementasi padding:
```html
div {
  padding: 10px; /* 10px space between the content and the border */
}
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flexbox dan grid layout merupakan dua teknik tata letak satu dimensi yang berfungsi untuk membuat desain web yang responsif dan lebih fleksibel. Mereka memiliki kegunaan dan cara kerja masing-masiung seperti berikut. 
  1. **Flexbox**
  Model tata letak satu dimensi yang memungkinkan elemen di dalam kontainer untuk disusun secara fleksibel. Dengan flexbox, Anda bisa mengatur susunan elemen baik secara horizontal maupun vertikal. Beberapa kegunaan dari flexbox adalah:
    - Menyusun elemen dalam satu baris atau kolom
    - Mengatur spasi antar elemen dengan mudah
    - Memusatkan elemen dalam kontainer
  2. **Grid Layout**
  Model tata letak dua dimensi yang memungkinkan Anda untuk membuat struktur grid (baris dan kolom) untuk menyusun elemen. Anda bisa mengatur ukuran, posisi, dan spasi elemen di dalam grid. Beberapa kegunaan  dari grid layout adalah:
    - Membuat tata letak yang kompleks dengan baris dan kolom
    - Memungkinkan penempatan elemen di posisi tertentu dalam grid
    - Membantu dalam desain responsif dengan menggunakan fraksi dan area grid

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [x] **Implementasikan fungsi untuk menghapus dan mengedit product.**
  1. Pada `views.py` tambahkan import:
  ```python
  from django.shortcuts import .., reverse
  from django.http import .., HttpResponseRedirect
  ```
  2. Pada `views.py` di subdirektori `main`, saya buat fungsi baru bernama `edit_album` yang berfungsi untuk edit sebuah album entry baru sebagai berikut:
  ```python
  def edit_album(request, id):
    # Get album entry berdasarkan id
    album = AlbumEntry.objects.get(pk = id)

    # Set album entry sebagai instance dari form
    form = AlbumEntryForm(request.POST or None, instance=album)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_album.html", context)
  ```
  3. Saya buat berkas html baru bernama `edit_album.html` pada subdirektori `templates` yang digunakan sebagai kerangka display fitur edit sebuah entry album. Isi dari berkas tersebut sebagai berikut:
  ```html
    {% extends 'base.html' %}

  {% load static %}

  {% block content %}

  <h1>Edit Album Entry</h1>

  <form method="POST">
      {% csrf_token %}
      <table>
          {{ form.as_table }}
          <tr>
              <td></td>
              <td>
                  <input type="submit" value="Edit Album Entry"/>
              </td>
          </tr>
      </table>
  </form>

  {% endblock %}
  ```
  4. Kemudian pada file `urls.py` saya import fungsi `edit_album` dari `views.py` kemudian menambahkan path agar jika tombol `edit` di klik pada aplikasi web akan dibawa ke halaman web edit album.
  5. Untuk menambahkan tombol `edit` yang saya sebutkan tadi, saya tambahkan pada berkas `main.html` seperti berikut:
  ```html
  <td>
      <a href="{% url 'main:edit_album' album_entry.pk %}">
          <button>
              Edit
          </button>
      </a>
  </td>
  ```
  6. Untuk menambahkan fitur hapus entry album, pada `views.py` saya tambahkan fungsi baru bernama `delete_album` yang berfungsi untuk menghapus entry album dari AlbumEntry sebagai berikut:
  ```python
  def delete_album(request, id):
    # Get album berdasarkan id
    album = AlbumEntry.objects.get(pk = id)
    # Hapus album
    album.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))
  ```
  7. Kemudian pada berkas `urls.py` saya import fungsi tersebut dari `views.py` dan tambahkan path tersendiri 
  8. Saya menambahkan tombol delete entry album pada berkas `main.html` sebagai berikut:
  ```html
  <td>
      <a href="{% url 'main:delete_album' album_entry.pk %}">
          <button>
              Delete
          </button>
      </a>
  </td>
  ```

- [x] **Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut:**
  Pada `base.html`, saya tambahkan tailwind sebagai framework CSS yang digunakan sebagai berikut:
  ```html
  <head>
  {% block meta %}
      <meta charset="UTF-8" />
      <meta name="viewport" content="width=device-width, initial-scale=1">
  {% endblock meta %}
  <script src="https://cdn.tailwindcss.com">
  </script>
  </head>
  ```
- [x] **Kustomisasi halaman login, register, dan tambah product semenarik mungkin.
  Dengan menggunakan CSS, saya kustomisasi halaman login sebagai berikut:**
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Login</title>
  {% endblock meta %}

  {% block content %}
  <div class="min-h-screen flex items-center justify-center w-screen bg-gray-800 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-gray-100">
          Login to your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST" action="">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          <div>
            <label for="username" class="sr-only">Username</label>
            <input id="username" name="username" type="text" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-500 placeholder-gray-400 text-gray-100 bg-gray-700 rounded-t-md focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm" placeholder="Username">
          </div>
          <div>
            <label for="password" class="sr-only">Password</label>
            <input id="password" name="password" type="password" required class="appearance-none rounded-none relative block w-full px-3 py-2 border border-gray-500 placeholder-gray-400 text-gray-100 bg-gray-700 rounded-b-md focus:outline-none focus:ring-red-500 focus:border-red-500 focus:z-10 sm:text-sm" placeholder="Password">
          </div>
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
            Sign in
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        {% if message.tags == "success" %}
          <div class="bg-green-900 border border-green-700 text-green-400 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% elif message.tags == "error" %}
          <div class="bg-red-900 border border-red-700 text-red-400 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% else %}
          <div class="bg-gray-900 border border-gray-700 text-gray-400 px-4 py-3 rounded relative" role="alert">
            <span class="block sm:inline">{{ message }}</span>
          </div>
        {% endif %}
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-gray-300">
          Don't have an account yet?
          <a href="{% url 'main:register' %}" class="font-medium text-red-400 hover:text-red-300">
            Register Now
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```
  Halaman register:
  ```html
  {% extends 'base.html' %}

  {% block meta %}
  <title>Register</title>
  {% endblock meta %}

  {% block content %}
  <div class="min-h-screen flex items-center justify-center bg-gray-100 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-md w-full space-y-8 form-style">
      <div>
        <h2 class="mt-6 text-center text-3xl font-extrabold text-black">
          Create your account
        </h2>
      </div>
      <form class="mt-8 space-y-6" method="POST">
        {% csrf_token %}
        <input type="hidden" name="remember" value="true">
        <div class="rounded-md shadow-sm -space-y-px">
          {% for field in form %}
            <div class="{% if not forloop.first %}mt-4{% endif %}">
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-black">
                {{ field.label }}
              </label>
              <div class="relative">
                {{ field }}
                <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                  {% if field.errors %}
                    <svg class="h-5 w-5 text-red-500" fill="currentColor" viewBox="0 0 20 20">
                      <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" />
                    </svg>
                  {% endif %}
                </div>
              </div>
              {% if field.errors %}
                {% for error in field.errors %}
                  <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                {% endfor %}
              {% endif %}
            </div>
          {% endfor %}
        </div>

        <div>
          <button type="submit" class="group relative w-full flex justify-center py-2 px-4 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            Register
          </button>
        </div>
      </form>

      {% if messages %}
      <div class="mt-4">
        {% for message in messages %}
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
          <span class="block sm:inline">{{ message }}</span>
        </div>
        {% endfor %}
      </div>
      {% endif %}

      <div class="text-center mt-4">
        <p class="text-sm text-black">
          Already have an account?
          <a href="{% url 'main:login' %}" class="font-medium text-indigo-200 hover:text-indigo-300">
            Login here
          </a>
        </p>
      </div>
    </div>
  </div>
  {% endblock content %}
  ```

  Tambah product:
  ```html
  {% extends 'base.html' %} 
  {`% load static %}
  {% block meta %}
  <title>Add New Album Entry</title>
  {% endblock meta %}

  {% block content %}
  {% include 'navbar.html' %}

  <div class="flex flex-col min-h-screen bg-gray-100">
    <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
      <h1 class="text-3xl font-bold text-center mb-8 text-black">Add New Album Entry</h1>

      <div class="bg-white shadow-md rounded-lg p-6 form-style">
        <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
            <div class="flex flex-col">
              <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                {{ field.label }}
              </label>
              <div class="w-full">
                {{ field }}
              </div>
              {% if field.help_text %}
                <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
              {% endif %}
              {% for error in field.errors %}
                <p class="mt-1 text-sm text-red-600">{{ error }}</p>
              {% endfor %}
            </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
            <button type="submit" class="bg-indigo-600 text-white font-semibold px-6 py-3 rounded-lg hover:bg-indigo-700 transition duration-300 ease-in-out w-full">
              Add Album Entry
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>

  {% endblock %}
  ```

- [x] **Kustomisasi halaman daftar product menjadi lebih menarik dan responsive. Kemudian, perhatikan kondisi berikut:**
 - Jika pada aplikasi belum ada product yang tersimpan, halaman daftar product akan menampilkan gambar dan pesan bahwa belum ada product yang terdaftar.
 - Jika sudah ada product yang tersimpan, halaman daftar product akan menampilkan detail setiap product dengan menggunakan card (tidak boleh sama persis dengan desain pada Tutorial!).

  Saya kustomisasi daftar produk dan halaman produk dengan menggunakan `main.html`, `card_album.html` dan `card_info.html`. `main.html` seperti ini:
  ```html
  {% extends 'base.html' %}
  {% load static %}

  {% block meta %}
  <title>Disco Paradise</title>
  {% endblock meta %}

  {% block content %}
  {% include 'navbar.html' %}

  <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen bg-gray-800 flex flex-col">
      <!-- Profile Information Section -->
      <div class="px-3 mb-4">
          <div class="flex rounded-md items-center bg-red-600 py-2 px-4 w-fit">
              <h1 id="nama-refalino-shahzada-ghassanai" class="text-white text-center">Nama: Refalino Shahzada Ghassanai</h1>
          </div>
          <h5 id="kelas-pbp-c" class="text-gray-300">Kelas: PBP C</h5>
      </div>

      <!-- Album Info Display -->
      <div class="p-2 mb-6 relative">
          <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
              {% include "card_info.html" with title='Nama' value=name %}
              {% include "card_info.html" with title='NPM' value=npm %}
              {% include "card_info.html" with title='Kelas' value=kelas %}
          </div>

          <div class="w-full px-6 absolute top-[44px] left-0 z-20 hidden md:flex">
              <div class="w-full min-h-4 bg-red-600"></div>
          </div>

          <div class="h-full w-full py-6 absolute top-0 left-0 z-20 md:hidden flex">
              <div class="h-full min-w-4 bg-red-600 mx-auto"></div>
          </div>
      </div>

      <!-- Last Login Section -->
      <div class="px-3 mb-4">
          <div class="flex rounded-md items-center bg-red-600 py-2 px-4 w-fit">
              <h1 id="last-login-last_login" class="text-white text-center">Last Login: {{last_login}}</h1>
          </div>
      </div>

      <!-- Add New Album Button -->
      <div class="flex justify-end mb-6">
          <a href="{% url 'main:create_album_entry' %}" class="bg-red-600 hover:bg-red-700 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out transform hover:-translate-y-1 hover:scale-105">
              Add New Album Entry
          </a>
      </div>

      <!-- Album List Section -->
      {% if album_entries %}
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6 space-y-6 w-full">
          <!-- Album Card Display -->
          {% for album_entry in album_entries %}
              {% include "card_album.html" with album_entry=album_entry %}
          {% endfor %}
      </div>
      {% else %}
      <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
          <img src="{% static 'image/sedih-banget.png' %}" alt="Sad face" class="w-32 h-32 mb-4">
          <p class="text-gray-300">Belum ada data album pada Disco Paradise.</p>
      </div>
      {% endif %}

      <!-- Logout Section -->
      <div class="flex justify-end mt-6">
          <a href="{% url 'main:logout' %}" class="bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg transition duration-300 ease-in-out">
              Logout
          </a>
      </div>
  </div>

  {% endblock content %}
  ```
  `card_info.html`:
  ```html
    <div class="bg-red-600 rounded-xl overflow-hidden border-2 border-red-700">
      <div class="p-4 animate-shine">
        <h5 class="text-lg font-semibold text-gray-200">{{ title }}</h5>
        <p class="text-gray-100">{{ value }}</p>
      </div>
    </div>
    ```
    `card_album.html`:
    ```html
    <div class="relative break-inside-avoid">
    <!-- Decorative Elements (No change needed) -->
    <div class="absolute top-2 z-10 left-1/2 -translate-x-1/2 flex items-center -space-x-2">
      <div class="w-[3rem] h-8 bg-gray-300 rounded-md opacity-80 -rotate-90"></div>
      <div class="w-[3rem] h-8 bg-gray-300 rounded-md opacity-80 -rotate-90"></div>
    </div>
    
    <!-- Main Album Card -->
    <div class="relative top-5 bg-gray-700 shadow-md rounded-lg mb-6 break-inside-avoid flex flex-col border-2 border-red-600 transform rotate-1 hover:rotate-0 transition-transform duration-300">
      <!-- Header Section (Title and Date) -->
      <div class="bg-red-600 text-gray-100 p-4 rounded-t-lg border-b-2 border-red-700">
        <h3 class="font-bold text-xl mb-2">{{album_entry.name}}</h3>
        <p class="text-gray-300">{{album_entry.date_of_distribution}}</p>
      </div>

      <!-- Album Info Section -->
      <div class="p-4">
        <p class="font-semibold text-lg mb-2 text-red-400">Price: ${{album_entry.price}}</p>
        <p class="text-gray-200 mb-2">
          <span class="bg-[linear-gradient(to_bottom,transparent_0%,transparent_calc(100%_-_1px),#FFEEEE_calc(100%_-_1px))] bg-[length:100%_1.5rem] pb-1">{{album_entry.description}}</span>
        </p>

        <!-- Stock and Genre Info -->
        <div class="mt-4">
          <p class="text-gray-300 font-semibold mb-2">Stock Available: {{album_entry.stock_available}}</p>
          <p class="text-gray-300 font-semibold">Genre: {{album_entry.genre}}</p>
        </div>
      </div>
    </div>

    <!-- Edit and Delete Buttons -->
    <div class="absolute top-0 -right-4 flex space-x-1">
      <a href="{% url 'main:edit_album' album_entry.pk %}" class="bg-yellow-500 hover:bg-yellow-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
        </svg>
      </a>
      <a href="{% url 'main:delete_album' album_entry.pk %}" class="bg-red-500 hover:bg-red-600 text-white rounded-full p-2 transition duration-300 shadow-md">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-9 w-9" viewBox="0 0 20 20" fill="currentColor">
          <path fill-rule="evenodd" d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z" clip-rule="evenodd" />
        </svg>
      </a>
    </div>
  </div>
  ```

- [x] **Untuk setiap card product, buatlah dua buah button untuk mengedit dan menghapus product pada card tersebut!**
Untuk melakukan hal tersebut, saya sudah kustomisasi pada step sebelumnya.

- [x] **Buatlah navigation bar (navbar) untuk fitur-fitur pada aplikasi yang responsive terhadap perbedaan ukuran device, khususnya mobile dan desktop.**
Untuk membuat navbar, saya mengisi berkas `navbar.html` sebagai berikut:
```html
<nav class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="flex items-center justify-between h-16">
    <div class="flex items-center">
      <a href="{% url 'main:show_main' %}" class="flex items-center">
        <h1 id="disco-paradise" class="text-2xl font-bold text-center text-white">Disco Paradise</h1>
      </a>
    </div>

    <div class="hidden md:flex items-center space-x-4">
      <a href="{% url 'main:show_main' %}" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Home</a>
      <a href="{% url 'main:create_album_entry' %}" class="text-gray-300 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium">Add Product</a>
      {% if user.is_authenticated %}
        <span class="text-gray-300 mr-4">Welcome, {{ user.username }}</span>
        <a href="{% url 'main:logout' %}" class="text-center bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
      {% else %}
        <a href="{% url 'main:login' %}" class="text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mr-2">Login</a>
        <a href="{% url 'main:register' %}" class="text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
      {% endif %}
    </div>

    <div class="md:hidden flex items-center">
      <button id="mobile-menu-button" class="text-gray-300 hover:bg-gray-700 hover:text-white px-2 py-1 rounded-md focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
        </svg>
      </button>
    </div>
  </div>
</nav>

<div id="mobile-menu" class="hidden md:hidden px-2 pt-2 pb-3 space-y-1 sm:px-3">
  <a href="{% url 'main:show_main' %}" class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Home</a>
  <a href="{% url 'main:create_album_entry' %}" class="text-gray-300 hover:bg-gray-700 hover:text-white block px-3 py-2 rounded-md text-base font-medium">Add Product</a>
  {% if user.is_authenticated %}
    <span class="block text-gray-300 px-3 py-2">Welcome, {{ user.username }}</span>
    <a href="{% url 'main:logout' %}" class="block text-center bg-gray-500 hover:bg-gray-600 text-white font-bold py-2 px-4 rounded transition duration-300">Logout</a>
  {% else %}
    <a href="{% url 'main:login' %}" class="block text-center bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded transition duration-300 mb-2">Login</a>
    <a href="{% url 'main:register' %}" class="block text-center bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded transition duration-300">Register</a>
  {% endif %}
</div>

<script>
  document.getElementById('mobile-menu-button').addEventListener('click', function() {
    var menu = document.getElementById('mobile-menu');
    menu.classList.toggle('hidden');
  });
</script>
```