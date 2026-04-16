from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.
def mensagem(request): 
    hora_atual = datetime.now().hour
    
    if hora_atual < 12:
        mensagem = "Bom dia!"
    elif hora_atual < 18:
        mensagem = "Boa tarde!"
    else:
        mensagem = "Boa noite!"
    return render(request, 'home.html', {'mensagem': mensagem})

def home(request):
    nome = 'Ana Maria'
    return render(request, 'home.html', {'nome': nome})

def saudacao(request, nome):
    mensagem = f'Olá, {nome}! Bem vindo ao nosso site.'
    return HttpResponse(mensagem)
    
    
def produtos(request, id_produto):
    
    produtos = {
        1:'Notbook',
        2:'Teclado',
        3:'Mouse',
        4:'Monitor',
        5:'Impressora',
        6:'Scanner',
        7:'Projetor',
        8:'Ar condicionado',
        9:'Forno',
        10:'Geladeira',
        11:'Lavadora',
        12:'Secadora',
    }
    
    produto = produtos.get(id_produto, 'Produto não encontrado')
    return HttpResponse(f'Detalhes do produto: {produto}')

def calcular(request, num1, num2, operacao):
    if operacao == 'soma':
        resultado = num1 + num2
    elif operacao == 'subtracao':
        resultado = num1 - num2
    elif operacao == 'multiplicacao':
        resultado = num1 * num2
    elif operacao == 'divisao':
        resultado = num1 / num2
    else:
        resultado = 'Operação inválida'
    return HttpResponse(f'Resultado: {resultado}')

def produtos(request):
    produtos = [
        'Notbook',
        'Teclado',
        'Mouse',
        'Monitor',
        'Impressora',
        'Scanner',
        'Projetor',
        'Ar condicionado',
        'Forno',
        'Geladeira',
    ]
    return render(request, 'produtos.html', {'produtos': produtos})