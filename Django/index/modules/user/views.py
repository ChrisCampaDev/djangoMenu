# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth.models import User
from django.db.models import Q

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    paginate_by = 8

    def get_queryset(self):
        listado = super().get_queryset()
        query = self.request.GET.get("q", "")
        if query:
            listado = listado.filter(
                Q(username=query)
            )
        return listado

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get("q", "")
        return context

class UserCreateView(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('user_list')

class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/form.html'
    success_url = reverse_lazy('user_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['is_staff'] = self.object.is_staff
        return kwargs

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'users/confirmDelete.html'
    success_url = reverse_lazy('user_list')