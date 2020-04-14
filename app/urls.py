from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    index, 
    home,  
    contact, 
    pesan,
    minta,
    aplicant,
    daftar,
)

urlpatterns = [
    # Parent
    path('', home, name='home'),
    path('pesan/', pesan, name='pesan' ),
    path('request/', minta, name='minta'),
    path('daftar/', daftar, name='daftar'),

    # Child
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'), 
    path('aplicant/', aplicant, name='aplicant'),
]

