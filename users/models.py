from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.username})

    def __str__(self):
        return self.username

    # class Meta:
    #     ordering = ["pk"]
