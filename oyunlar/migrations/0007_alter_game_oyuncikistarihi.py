# Generated by Django 4.2 on 2023-07-23 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0006_alter_comment_commentedgame'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='oyunCikisTarihi',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oyunlar.releasedate'),
        ),
    ]