from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .forms import DaftarForm, PesanForm, MintaForm
from .models import Daftar, Pesan, Minta

# Parent
def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def aplicant(request):
    return render(request, 'minta.html')



# Child
def minta(request):
    mintakonten = Minta.objects.order_by('-buat')[:4]
    form = MintaForm()
    if request.method == 'POST':
        form = MintaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("minta"))

    context = { 'form': form, 'request': minta }
    return render(request, 'request.html', context)

def daftar(request):
    form = DaftarForm()
    if request.method == 'POST':
        form = DaftarForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("daftar"))
    context = { 'form': form }
    return render(request, 'daftar.html', context)

def home(request):
    profile = Daftar.objects.order_by('-buat')[:4]
    context = {'profile': profile}
    return render(request, 'home.html', context)

def pesan(request):
    form = PesanForm()
    if request.method == 'POST':
        form = PesanForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("pesan"))

    context = {'form': form}
    return render(request, 'pesan.html', context)




  