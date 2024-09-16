from django.shortcuts import render, redirect
from main.forms import AlbumEntryForm
from main.models import AlbumEntry
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
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

def create_album_entry(request):
    form = AlbumEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    context = {'form': form}
    return render(request, "create_album_entry.html", context)

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