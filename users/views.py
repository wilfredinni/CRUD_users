from django.views.generic import ListView, DetailView

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
