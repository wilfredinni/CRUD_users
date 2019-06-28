from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class Perfil(models.Model):
    perfil_name = models.SlugField(unique=True)

    def __str__(self):
        return self.perfil_name

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    perfil = models.ManyToManyField(Perfil)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.username})

    def __str__(self):
        return self.username

    class Meta:
        ordering = ["pk"]
