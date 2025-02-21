# views.py
from django.shortcuts import  render
from django.views.generic import TemplateView

from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .form import ComentarioForm
from index.modules.products.models import Producto
from django.contrib.auth.models import User

from django.core.paginator import Paginator

from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

class HomeView(TemplateView):
    template_name = 'index.html'

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/login.html', {'form': form})
    return render(request, 'registration/login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        return render(request, 'registration/register.html', {'form': form})
    return render(request, 'registration/register.html')


@login_required
@user_passes_test(lambda u: u.is_staff)  # Solo para usuarios administradores
def admin_dashboard(request):
    # Filtros para usuarios
    query_usuario = request.GET.get('q_usuario', '')
    usuarios = User.objects.all()
    if query_usuario:
        usuarios = usuarios.filter(
            Q(username__icontains=query_usuario) |
            Q(email__icontains=query_usuario)
        )
    # Filtros para productos
    query_producto = request.GET.get('q_producto', '')
    tipo_producto = request.GET.get('tipo_producto', '')
    productos = Producto.objects.all()
    if query_producto:
        productos = productos.filter(nombre__icontains=query_producto)
    if tipo_producto:
        productos = productos.filter(tipo=tipo_producto)

    # Estadísticas
    total_usuarios = User.objects.count()
    total_productos = Producto.objects.count()

    context = {
        'total_usuarios': total_usuarios,
        'total_productos': total_productos,
        'usuarios': usuarios,
        'productos': productos,
        'query_usuario': query_usuario,
        'query_producto': query_producto,
        'tipo_producto': tipo_producto,
    }
    return render(request, 'admin.html', context)

def UserLogout(request):
    logout(request)
    return redirect('home')

def lista_productos(request):
    productos_list = Producto.objects.all()
    paginator = Paginator(productos_list, 8)  # Muestra 8 productos por página
    page = request.GET.get('page')
    productos = paginator.get_page(page)
    return render(request, 'list_food.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    comentarios = producto.comentarios.all().order_by('-fecha_creacion')

    if request.method == 'POST' and request.user.is_authenticated:
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.producto = producto
            comentario.usuario = request.user
            comentario.save()
            return redirect('detalle_producto', producto_id=producto.id)
    else:
        form = ComentarioForm()

    context = {
        'producto': producto,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'detalle_producto.html', context)