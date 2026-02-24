from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_prestamos, name='lista_prestamos'),
    path('crear/', views.crear_prestamo, name='crear_prestamo'),
    path('devolver/<int:id>/', views.devolver_libro, name='devolver_libro'),
]