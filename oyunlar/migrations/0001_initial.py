# Generated by Django 4.2 on 2023-07-04 14:40

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReleaseDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cikisTarihi', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oyunIsim', models.CharField(max_length=100)),
                ('oyunAciklama', ckeditor.fields.RichTextField(max_length=500)),
                ('oyunResim', models.ImageField(upload_to='oyunlar/')),
                ('oyunCikisTarihi', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oyunlar.releasedate')),
                ('oyunPlatformu', models.ManyToManyField(blank=True, to='oyunlar.platform')),
                ('oyunTuru', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oyunlar.genre')),
            ],
        ),
    ]
