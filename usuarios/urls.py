from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_estudiantes, name='lista_estudiantes'),
    path('crear/', views.crear_estudiante, name='crear_estudiante'),
    path('editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),
]