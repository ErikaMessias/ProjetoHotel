from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('hoteis/', views.hoteis, name='hoteis'),
    path('reserva/', views.reserva, name='reserva'),
    path('cadastrar/', views.cad_user, name='user'),
    path('formulario', views.insere_cliente, name='insere_cliente'),
    path('cad_reserva/', views.insere_reserva, name='insere_reserva'),
    path('<int:id>', views.deleta_cliente, name='deleta_cliente'),
    path('reserva/<int:id>', views.deleta_reserva, name='deleta_reserva'),
]