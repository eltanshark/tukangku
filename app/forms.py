from django.forms import ModelForm


from .models import Daftar, Pesan

class DaftarForm(ModelForm):
    class Meta:
        model = Daftar
        fields = '__all__'

class PesanForm(ModelForm):
    class Meta:
        model = Pesan
        fields = '__all__'