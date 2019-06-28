from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Perfil


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email"]
    fieldsets = ((None, {"fields": ("username", "password", "email", "perfil")}),)
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "email", "perfil"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Perfil)
