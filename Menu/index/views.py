# views.py
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
#from django.contrib.auth import login, authenticate, logout
#from django.shortcuts import redirect, render

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'index.html'
    login_url = 'login'

class UserLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('base')

class UserLogoutView(LogoutView):
    next_page = reverse_lazy('login')
