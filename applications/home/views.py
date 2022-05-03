from dataclasses import fields
from pyexpat import model
from re import template
from typing import Generic
from django import views
from django.shortcuts import render
from django.views.generic import (
    TemplateView, ListView, CreateView
)
# import models 
from .models import Prueba
from .forms import PruebaForm

# Create your views here.

class PruebaView(TemplateView):
    
    #hace referencia a un html
    template_name = 'home/prueba.html'

class PruebaListView(ListView):
    #model = Model
    template_name = "home/lista.html"
    
    context_object_name = 'listaNumeros'
    ##todo el queryset se guarda en la variable listaNumeros para ser leido en el html
    queryset = ['1','10','20','30','40','50']

class ListaPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'

class PruebaCreateView(CreateView):
    template_name = 'home/add.html'
    model = Prueba
    #le conecto al formulario PruebaForm
    form_class = PruebaForm
    success_url = '/'


class ResumeFoundationView(TemplateView):
    
    #hace referencia a un html
    template_name = 'home/resumen_foundation.html'
    