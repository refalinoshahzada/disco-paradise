from django.db import models

class AlbumEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    date_of_distribution = models.TextField()
    stock_available = models.IntegerField()
    genre = models.TextField()