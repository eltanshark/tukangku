from django.forms import ModelForm


from .models import Daftar, Pesan, Minta

class DaftarForm(ModelForm):
    class Meta:
        model = Daftar
        fields = '__all__'

class PesanForm(ModelForm):
    class Meta:
        model = Pesan
        fields = '__all__'

class MintaForm(ModelForm):
    class Meta:
        model = Minta
        fields = '__all__'