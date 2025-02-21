# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.contrib.auth.models import User

class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'users/list.html'
    context_object_name = 'users'
    paginate_by = 8

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