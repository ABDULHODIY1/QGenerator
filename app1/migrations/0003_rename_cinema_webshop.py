# Generated by Django 4.1.6 on 2023-06-07 17:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cinema',
            new_name='WebShop',
        ),
    ]
