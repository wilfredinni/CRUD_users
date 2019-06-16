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


class UserList(ListView):
    model = CustomUser
    template_name = "users/list_users.html"
    context_object_name = "users"


class UserDetail(DetailView):
    model = CustomUser
    template_name = "users/user.html"
    context_object_name = "user"
    slug_field = "username"


class CreateUser(CreateView):
    model = CustomUser
    template_name = "users/create_user.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("users")


class UpdateUser(UpdateView):
    model = CustomUser
    template_name = "users/create_user.html"
    fields = ["username", "email", "bio"]
    slug_field = "username"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context


class DeleteUser(DeleteView):
    model = CustomUser
    template_name = "users/delete_user.html"
    success_url = reverse_lazy("users")
    slug_field = "username"
