from django.urls import path
from . import views

urlpatterns = [
    path('metodos-pago/', views.lista_metodos, name='lista_metodos'),
    path('metodos-pago/crear/', views.crear_metodo, name='crear_metodo'),
    path('metodos-pago/editar/<int:id>/', views.editar_metodo, name='editar_metodo'),
    path('metodos-pago/eliminar/<int:id>/', views.eliminar_metodo, name='eliminar_metodo'),
]
