from django.forms import ModelForm
from main.models import AlbumEntry
from django.utils.html import strip_tags

class AlbumEntryForm(ModelForm):
    class Meta:
        model = AlbumEntry
        fields = ["name", "price", "description", "date_of_distribution", "stock_available", "genre"]
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)
    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    def clean_date_of_distribution(self):
        date_of_distribution = self.cleaned_data["date_of_distribution"]
        return strip_tags(date_of_distribution)
    def clean_stock_available(self):
        stock_available = self.cleaned_data["stock_available"]
        return strip_tags(stock_available)
    def clean_genre(self):
        genre = self.cleaned_data["genre"]
        return strip_tags(genre)