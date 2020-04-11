from django.shortcuts import render


from .forms import DaftarForm, PesanForm
from .models import Daftar

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    form = DaftarForm()
    profile = Daftar.objects.order_by('-buat')[:4]
    if request.method == 'POST':
        form = DaftarForm(request.POST)
        if form.is_valid():
            form.save()
            form = DaftarForm()

    context = {'form': form, 'profile': profile}
    return render(request, 'daftar.html', context)

def pesan(request):
    psn = PesanForm()
    if request.method == 'POST':
        psn = PesanForm(request.POST)
        if psn.is_valid():
            psn.save()
            psn = PesanForm()

    context = {'psn': psn}
    return render(request, 'contact.html', context)
  