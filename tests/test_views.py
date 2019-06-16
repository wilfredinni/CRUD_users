from django.test import TestCase, Client
from django.urls import reverse

from users.models import CustomUser


class TestNonAuthenticatedViews(TestCase):
    """comprobar que las vistas están protegidas"""

    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user("test_user")

    def test_users_list(self):
        url = reverse("users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_user_detail(self):
        url = reverse("profile", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_create_user(self):
        url = reverse("new")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update_user(self):
        url = reverse("update", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_user(self):
        url = reverse("delete", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)


class TestAuthenticatedViews(TestCase):
    """Las vistas y templates pueden ser accedidos si el usuario está autenticado"""

    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user(username="test_user", password="pass")
        self.client.login(username="test_user", password="pass")

    def test_users_list(self):
        url = reverse("users")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/list_users.html")

    def test_user_detail(self):
        url = reverse("profile", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/user.html")

    def test_create_user(self):
        url = reverse("new")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create_user.html")

    def test_update_user(self):
        url = reverse("update", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/create_user.html")

    def test_delete_user(self):
        url = reverse("delete", args=["test_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "users/delete_user.html")
