from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy

#from Menu.utils.utils import update_paginate
from .models import Producto
from .form import ProductoForm


class ProductoListView(ListView,PermissionRequiredMixin,LoginRequiredMixin):
    model = Producto
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 8

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