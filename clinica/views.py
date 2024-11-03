from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse('ola mundo doido   geral da home!')
    return render(request ,'home.html')

def paciente(request):
    #return HttpResponse('ola mundo doido paciente!')
    return render(request ,'paciente.html')

def medico(request):
    #return HttpResponse('ola mundo doido medico!')
    return render(request ,'medico.html')

def proprietario(request):
    #return HttpResponse('ola mundo doido  prietario!')
    return render(request ,'proprietario.html')

def login(request):

    return render(request ,'login.html')











