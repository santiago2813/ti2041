# Generated by Django 4.2.5 on 2023-11-10 00:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Blog_Personal", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Post",
            new_name="Publicacion",
        ),
    ]
