# Generated by Django 5.1.2 on 2024-10-11 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='photos',
            new_name='photo',
        ),
    ]
