from django.urls import path
from aparelhos import views

app_name = 'aparelhos'

urlpatterns = [
    path('consumo/<slug:slug>/', views.simulator, name='teste'),
    path('', views.lista_Aparelho, name='lista_aparelhos'),
    path('cadastrar-aparelho/', views.cadastro_Aparelho, name='save_aparelho'),
    path('alterar/<int:pk>/', views.edit_aparelho, name='edit_aparelho'),
    path('apagar/<int:pk>/', views.deletar_aparelho, name='deletar_aparelho'),
    path('insercao-aparelho-ambiente/', views.relation, name='relation'),
    
]