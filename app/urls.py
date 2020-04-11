from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .views import (
    index, 
    home,  
    contact, 
)

urlpatterns = [
    path('', home, name='home'),
    path('index/', index, name='index'),
    path('contact/', contact, name='contact'), 
]

