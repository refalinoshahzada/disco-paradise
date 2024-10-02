from django.shortcuts import render, redirect, reverse
from main.forms import AlbumEntryForm
from main.models import AlbumEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    album_entries = AlbumEntry.objects.filter(user=request.user)

    context = {
        'name': request.user.username,
        'npm': 2306152203,
        'kelas': 'PBP C',
        'last_login': request.COOKIES['last_login'],
        'album_entries': album_entries
    }

    return render(request, "main.html", context)

# Create album entry
def create_album_entry(request):
    form = AlbumEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        album_entry = form.save(commit=False)
        album_entry.user = request.user
        album_entry.save()
        return redirect("main:show_main")
    
    context = {'form': form}
    return render(request, "create_album_entry.html", context)

# Show data through XML and JSON
def show_xml(request):
    data = AlbumEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = AlbumEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = AlbumEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = AlbumEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# Register User
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

# Login User
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

# Logout User
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

# Edit Album
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

# Delete Album
def delete_album(request, id):
    # Get album berdasarkan id
    album = AlbumEntry.objects.get(pk = id)
    # Hapus album
    album.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))