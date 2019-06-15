from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import CustomUserCreationForm
from .models import CustomUser


class UserList(ListView):
    model = CustomUser
    template_name = "list_users.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = CustomUser
    template_name = "user.html"
    context_object_name = "user"
    slug_field = "username"


class UserCreate(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users")
    template_name = "create_user.html"


class DeleteUser(DeleteView):
    model = CustomUser
    success_url = reverse_lazy("users")
    template_name = "delete_user.html"
    slug_field = "username"
