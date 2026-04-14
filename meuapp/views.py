from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def home(request): 
    hora_atual = datetime.now().hour
    
    if hora_atual < 12:
        mensagem = "Bom dia!"
    elif hora_atual < 18:
        mensagem = "Boa tarde!"
    else:
        mensagem = "Boa noite!"
    return HttpResponse(f"{mensagem} Agora são {hora_atual} horas.")