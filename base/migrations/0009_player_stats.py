# Generated by Django 4.2 on 2023-04-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_game_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='stats',
            field=models.TextField(blank=True, null=True),
        ),
    ]