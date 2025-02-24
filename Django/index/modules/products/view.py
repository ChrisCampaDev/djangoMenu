from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

#from Menu.utils.utils import update_paginate
from .models import Producto
from .form import ProductoForm
from django.db.models import Q


class ProductoListView(ListView,PermissionRequiredMixin,LoginRequiredMixin):
    model = Producto
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        listado = super().get_queryset()
        query = self.request.GET.get("q", "")
        tipo_filter = self.request.GET.get("tipo_filter", "")

        if tipo_filter:
            listado = listado.filter(tipo=tipo_filter)

        if query:
            listado = listado.filter(
                Q(nombre=query)|
                Q(tipo=query)
            )
        return listado

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q", "")
        context['tipos_productos'] = Producto.get_type_choices()
        return context


class ProductoCreateView(CreateView,LoginRequiredMixin,SuccessMessageMixin):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Producto creado exitosamente"

class ProductoUpdateView(UpdateView,LoginRequiredMixin,SuccessMessageMixin):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')
    success_message = "Producto editado exitosamente"

class ProductoDeleteView(DeleteView,LoginRequiredMixin):
    model = Producto
    template_name = 'product/confirmDelete.html'
    success_url = reverse_lazy('product_list')