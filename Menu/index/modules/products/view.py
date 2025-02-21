from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

#from Menu.utils.utils import update_paginate
from .models import Producto
from .form import ProductoForm


class ProductoListView(ListView,PermissionRequiredMixin,LoginRequiredMixin):
    model = Producto
    template_name = 'product/list.html'
    context_object_name = 'products'
    paginate_by = 8

class ProductoCreateView(CreateView,LoginRequiredMixin):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')

class ProductoUpdateView(UpdateView,LoginRequiredMixin):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')

class ProductoDeleteView(DeleteView,LoginRequiredMixin):
    model = Producto
    template_name = 'product/confirmDelete.html'
    success_url = reverse_lazy('product_list')