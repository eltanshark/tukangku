# Generated by Django 3.0 on 2020-04-12 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20200412_0853'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daftar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('telepon', models.CharField(max_length=13)),
                ('alamat', models.TextField()),
                ('umur', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=1)),
                ('posisi', models.CharField(max_length=50)),
                ('buat', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(default='upload/default-image.jpg', upload_to='upload/')),
            ],
            options={
                'verbose_name_plural': 'Data-Daftar',
            },
        ),
        migrations.CreateModel(
            name='Pesan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subjek', models.CharField(blank=True, max_length=100, null=True)),
                ('pesan', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Data-Pesan',
            },
        ),
    ]