# views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

from index.modules.products.models import Producto
from django.core.paginator import Paginator


class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    login_url = 'login'

class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('base')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')

def lista_productos(request):
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 8)  # Muestra 8 productos por página
    page = request.GET.get('page')
    productos = paginator.get_page(page)
    return render(request, 'list_food.html', {'productos': productos})
