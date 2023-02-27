from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('registrarPrograma/', views.registrarPrograma),
    path('editarPrograma/<Nombre>', views.editarPrograma),
    path('edicionPrograma/',views.edicionPrograma),
    path('eliminarPrograma/<Nombre>', views.eliminarPrograma),
] 
