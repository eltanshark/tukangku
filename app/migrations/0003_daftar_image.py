# Generated by Django 3.0 on 2020-04-08 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200408_1238'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftar',
            name='image',
            field=models.ImageField(default='static/upload/', upload_to='static/upload/tkg/'),
        ),
    ]
