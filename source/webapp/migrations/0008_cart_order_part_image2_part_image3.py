# Generated by Django 5.0.6 on 2024-09-21 11:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webapp", "0007_order_orderpart"),
    ]

    operations = [
        migrations.AddField(
            model_name="part",
            name="image2",
            field=models.ImageField(blank=True, null=True, upload_to="parts/"),
        ),
        migrations.AddField(
            model_name="part",
            name="image3",
            field=models.ImageField(blank=True, null=True, upload_to="parts/"),
        ),
    ]
