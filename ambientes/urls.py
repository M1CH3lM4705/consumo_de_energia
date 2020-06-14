from django.urls import path
from ambientes import views

app_name = 'ambientes'

urlpatterns = [
    path('', views.index, name='index'),
    path('ambientes/cadastrar/', views.Cadastrar_ambiente, name='save_ambiente'),
    path('ambientes/apagar/<int:pk>/', views.deletar_ambiente, name='del_ambiente'),
    path('ambientes/alterar/<int:pk>/', views.editar_ambiente, name='edit_ambiente'),
    path('ambientes/<slug:slug>/', views.select_ambiente, name='select_ambiente'),
]