# Generated by Django 5.0.6 on 2024-07-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
