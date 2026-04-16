from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('saudacao/<str:nome>/', views.saudacao, name='saudacao'),
    path('produtos/<int:id_produto>/', views.produtos, name='produtos'),
    path('calcular/<int:num1>/<int:num2>/<str:operacao>/', views.calcular, name='calcular'),
    path('mensagem/', views.mensagem, name='mensagem'),
    path('produtos/', views.produtos, name='produtos'),
]