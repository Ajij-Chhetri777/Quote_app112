# Generated by Django 5.0.3 on 2024-04-06 12:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_favourite_favourite_favourite_favourite_item_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='quotes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quota', to='app.quote'),
        ),
    ]