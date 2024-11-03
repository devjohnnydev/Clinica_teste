from django.urls import path
from django.http import HttpResponse
from clinica.views import home, paciente, medico, proprietario,login



urlpatterns = [
    path('', home , name='home'),
    path('paciente/', paciente, name='paciente'),
    path('medico/', medico),
    path('proprietario/', proprietario),
    path('login/', login, name='login'),
   
]
