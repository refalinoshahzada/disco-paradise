from django.forms import ModelForm
from main.models import AlbumEntry

class AlbumEntryForm(ModelForm):
    class Meta:
        model = AlbumEntry
        fields = ["name", "price", "description", "date_of_distribution", "stock_available", "genre"]