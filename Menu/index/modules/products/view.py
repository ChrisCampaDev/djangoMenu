from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto
from .form import ProductoForm

class ProductoListView(ListView):
    model = Producto
    template_name = 'product/list.html'
    context_object_name = 'products'

class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')

class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'product/form.html'
    success_url = reverse_lazy('product_list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'product/confirmDelete.html'
    success_url = reverse_lazy('product_list')