from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    DeleteView,
    UpdateView,
)

from .forms import CustomUserCreationForm
from .models import CustomUser


class UserList(LoginRequiredMixin, ListView):
    template_name = "users/list_users.html"
    context_object_name = "users"
    paginate_by = 5

    def get_queryset(self):
        queryset = CustomUser.objects.all()
        # los usuarios que no son staff solo pueden ver
        # y editar sus propios perfiles
        if not self.request.user.is_superuser:
            queryset = queryset.filter(username=self.request.user.username)

        return queryset


class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = "users/user.html"
    context_object_name = "user"
    slug_field = "username"


class CreateUser(LoginRequiredMixin, CreateView):
    model = CustomUser
    template_name = "users/create_user.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users")


class UpdateUser(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = "users/create_user.html"
    fields = ["username", "email", "bio"]
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users")
    slug_field = "username"
