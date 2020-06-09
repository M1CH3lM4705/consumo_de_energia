from django.urls import path
from aparelhos import views

app_name = 'aparelhos'

urlpatterns = [
    path('simulador/', views.calcSimulador, name='calcSimulador'),
    path('cadastrar-aparelho/', views.cadastroAparelho, name='cadastro'),  
    path('detalhes/', views.detalheAparelho, name='lista-aparelhos'),
]