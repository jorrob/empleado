from django.contrib import admin
from django.urls import path
from . import views

def DesdeApps(self):
    print("=================Desde App Persona=======================")

app_name = "personas_app"

urlpatterns = [
    path(
        '',
        views.InicioView.as_view(),
        name='inicio'
        ),
    path(
        'listar-todo-empleados/',
        views.ListAllEmpleados.as_view(),
        name= 'empleados_all'
        ),
    path(
        'lista-empleados-admin/',
        views.ListaEmpleadosAdmin.as_view(),
        name= 'empleados_admin'
    ),
    path('listar-by-area/',views.ListByAreaEmpleado.as_view()),
    path('listar-by-area-metodo/',views.ListByAreaEmpleadoMetodo.as_view()),
    path(
        'listar-by-area-get/<namedepa>',
        views.ListByAreaEmpleadoGET.as_view(),
        name='empleados_area',
        ),
    path('buscar-empleado/',views.ListEmpleadosByKword.as_view()),
    path('listar-habilidades/',views.ListaHabilidadesEmpleado.as_view()),
    path(
        'ver-empleado/<pk>',
         views.EmpleadoDetailView.as_view(),
         name = "empleado_detalle"
         ),
    path(
        'add-empleado/',
        views.EmpleadoCreateView.as_view(),
        name= "empleado_add"
        ),
    path(
        'success/',
        views.SuccessView.as_view(),
        name='correcto'
        ),

    path(
        'update-empleado/<pk>/',
        views.EmpleadoUpdateView.as_view(),
        name='modificar_empleado'
        ),
    
    path(
        'delete-empleado/<pk>/',
        views.EmpleadoDetailViewDelete.as_view(),
        name='delete_empleado'
        ),
    

]

