# Generated by Django 4.2 on 2023-07-11 12:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0002_alter_game_oyunaciklama'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='oyunAciklama',
            field=ckeditor.fields.RichTextField(max_length=10000),
        ),
    ]