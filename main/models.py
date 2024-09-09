from django.db import models

class MoodEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.DateField(auto_now_add=True)
    description = models.TextField()
    data_of_distribution = models.TextField()
    stock_available = models.IntegerField()
    genre = models.TextField()