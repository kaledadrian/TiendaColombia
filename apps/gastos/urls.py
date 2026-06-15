from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('gastos/', views.lista_gastos, name='lista_gastos'),
    path('gastos/crear/', views.crear_gasto, name='crear_gasto'),
    path('gastos/editar/<int:id>/', views.editar_gasto, name='editar_gasto'),
    path('gastos/eliminar/<int:id>/', views.eliminar_gasto, name='eliminar_gasto'),

    path('reportes/', views.reportes, name='reportes'),
]
