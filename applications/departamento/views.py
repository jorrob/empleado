from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento

# Create your views here.
#vista generica formview

class DepartamentoListView(ListView):
    template_name = 'departamento/listar-departamento.html'
    # paginate_by = 5
    model = Departamento
    context_object_name = 'departamento'



class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        print ('****************** estamos en el form valid****************')
        
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shortname = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellido']
        
        
        #Registrio la informcion
        Empleado.objects.create(
            first_name = nombre, 
            last_name = apellido,
            job = '1',
            departamento = depa
            )
        return super(NewDepartamentoView,self).form_valid(form)
