from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    judul       = models.CharField(max_length=200)
    sub_judul   = models.CharField(max_length=200)
    konten      = models.TextField()
    pub_date    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.judul 

    class Meta:
        verbose_name_plural = 'Buat-Post'

class Banner(models.Model):
    judul       = models.CharField(max_length=50)
    isi         = models.TextField()
    image       = models.ImageField(upload_to='upload/', default='upload/default-image.jpg')

    def __str__(self):
        return self.judul

    class Meta:
        verbose_name_plural = 'Buat-Banner'

# Form Section
class Daftar(models.Model):
    nama        = models.CharField(max_length=200, )
    email       = models.EmailField()
    telepon     = models.CharField(max_length=13)
    alamat      = models.TextField()
    umur        = models.CharField(max_length=3)
    gender      = models.CharField(max_length=1)
    posisi      = models.CharField(max_length=50)
    buat        = models.DateTimeField(auto_now=True)
    image       = models.ImageField(upload_to='upload/', default='upload/default-image.jpg')

    def __str__(self):
        return self.nama + ' -- ' + self.email + ' -- ' + self.alamat
    
    class Meta:
        verbose_name_plural = 'Data-Daftar'

class Pesan(models.Model):
    nama        = models.CharField(max_length=100)
    email       = models.EmailField()
    subjek      = models.CharField(max_length=100, blank=True, null=True)
    pesan       = models.TextField()

    def __str__(self):
        return self.nama + ' -- ' + self.email
    
    class Meta:
        verbose_name_plural = 'Data-Pesan'


