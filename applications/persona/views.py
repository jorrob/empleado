from multiprocessing import context
from xml.parsers.expat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )


# Create your views here.

class InicioView(TemplateView):
    template_name = 'inicio.html'

#1 listar todos los empreados de la empresa
from .models import Empleado
from .form import EmpleadoForm 

#listar todos los empleados
class ListAllEmpleados(ListView):
    template_name = 'persona/list-all.html'
    paginate_by = 5
    ordering = "Last_name"
    #objeto de paginacion
    context_object_name = 'empleados'
    #model = Empleado
    #context_object_name = 'lista'
    #http://127.0.0.1:8000/listar-todo-empleados/?page=2
    def get_queryset(self):
        
        palabra_clave = self.request.GET.get("kword", '')
        # jorge = j 
        print (palabra_clave)
        lista = Empleado.objects.filter(
            #first_name = palabra_clave
            full_name__icontains = palabra_clave
            
        )
        print(lista)
        return lista

class ListaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = "last_name"
    #objeto de paginacion
    context_object_name = 'empleados'
    #si no hay queryset debe existir model
    model = Empleado

    
#listar todos los empelados que pertenecen a un area
class ListByAreaEmpleado (ListView):
    template_name = 'persona/list-by-area.html'
    queryset = Empleado.objects.filter(
        #departamento_name= 'finanzas'
        #departamento_id= 1
        departamento__name= 'finanzas'
    )


#listar todos los empelados que pertenecen a un area con metodo
class ListByAreaEmpleadoMetodo(ListView):
    template_name = 'persona/list-by-area-metodo.html'    
    def get_queryset(self):
        lista = Empleado.objects.filter(
            departamento__name= 'Administrativo'
        )
        return lista

#filtrado por url
class ListByAreaEmpleadoGET(ListView):
    template_name = 'persona/list-by-area-get.html'
    context_object_name = 'empleados'    
    def get_queryset(self):
        #variable tomada por url
        nombre = self.kwargs['namedepa']
        lista = Empleado.objects.filter(
            departamento__name= nombre
        )
        print('lista resultado:',lista)
        return lista
        #http://127.0.0.1:8000/listar-by-area-get/Administrativo


class ListEmpleadosByKword(ListView):
    #listar empleados por palabra clave
    template_name = 'persona/by-kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        print('****************************')
        palabra_clave = self.request.GET.get("kword", '')
        print (palabra_clave)
        lista = Empleado.objects.filter(
            first_name = palabra_clave
        )
        print('lista resultado:',lista)
        return lista

#Lista de empleados y habilidades many to many
class ListaHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        print('------------ empleado: ',palabra_clave)
        empleado = Empleado.objects.get(first_name=palabra_clave)
        print(empleado)
        return empleado.habilidades.all()
        #return []
        #)

#****************************************************************
#DETAILVIEW

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail-empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'empleado del mes'
        return context
#http://127.0.0.1:8000/ver-empleado/1


#****************************************************************
#CREATEVIEW

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/add.html"
    form_class = EmpleadoForm
    #fields = ('__all__')
    #redirecciona a SuccessView
    success_url = reverse_lazy('personas_app:empleados_admin')

    def form_valid(self, form):
        #los registris guardados le asigno a la variable empleado
        empleado = form.save(commit='false')
        #print(empleado)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        #se guarda en la base de datos directo
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)
#****************************************************************
#Redirigir a una nueva vista 

class SuccessView(TemplateView):
    template_name = "persona/success.html"


#***************************************************************
#updateview
class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/update.html"
    form_class = EmpleadoForm
    success_url = reverse_lazy('personas_app:empleados_admin')

    #interseptar el proceso antes de que se guarden los datos
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print ('******************************Metodo Post**********************************')
        print (request.POST)
        print (request.POST['last_name'])
        print ('===========================================================================')
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        print ('******************************Metodo FORM_valid****************************')
        print ('***************************************************************************')
        print (self.get_object())
        return super(EmpleadoUpdateView,self).form_valid(form)

class EmpleadoDetailViewDelete(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('personas_app:empleados_admin')