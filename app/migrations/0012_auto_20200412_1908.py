# Generated by Django 3.0 on 2020-04-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200412_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='daftar',
            name='gender',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='daftar',
            name='posisi',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]