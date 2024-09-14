# Generated by Django 5.1.1 on 2024-09-14 15:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumEntry',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DateField(auto_now_add=True)),
                ('description', models.TextField()),
                ('date_of_distribution', models.TextField()),
                ('stock_available', models.IntegerField()),
                ('genre', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='MoodEntry',
        ),
    ]
