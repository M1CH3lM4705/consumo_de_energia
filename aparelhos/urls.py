from django.urls import path
from aparelhos import views

app_name = 'aparelhos'

urlpatterns = [
    path('consumo/', views.calcSimulador, name='calcSimulador'),
    path('', views.lista_Aparelho, name='lista_aparelhos'),
    path('cadastrar-aparelho/', views.cadastro_Aparelho, name='save_aparelho'),
    path('/alterar/<int:pk>/', views.edit_aparelho, name='edit_aparelho'),
    
]