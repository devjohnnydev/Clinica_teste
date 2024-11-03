from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import Group

# Criar grupo se não existir
grupo_paciente, created = Group.objects.get_or_create(name='Paciente')
