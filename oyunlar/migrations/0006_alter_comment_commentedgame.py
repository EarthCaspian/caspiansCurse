# Generated by Django 4.2 on 2023-07-18 18:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oyunlar', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='commentedGame',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='oyunlar.game'),
        ),
    ]
