from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('registrarPrograma/', views.registrarPrograma),
    path('editarPrograma/<Nombre>', views.editarPrograma),
    path('edicionPrograma/',views.edicionPrograma),
    path('eliminarPrograma/<Nombre>', views.eliminarPrograma),
]
