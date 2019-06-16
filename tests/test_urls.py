from django.test import TestCase, Client
from django.urls import resolve, reverse

from users.views import UserList, UserDetail, CreateUser, UpdateUser, DeleteUser
from users.models import CustomUser


class UsersUrlsTest(TestCase):
    """comprobar que las vistas rendidas por las vistas que corresponden"""
    def setUp(self):
        self.client = Client()
        CustomUser.objects.create_user("test_user")

    def test_userlist_url(self):
        url = reverse("users")
        self.assertEqual(resolve(url).func.view_class, UserList)

    def test_userdetail_url(self):
        url = reverse("profile", args=["test_user"])
        self.assertEqual(resolve(url).func.view_class, UserDetail)

    def test_createuser_url(self):
        url = reverse("new")
        self.assertEqual(resolve(url).func.view_class, CreateUser)

    def test_updateuser_url(self):
        url = reverse("update", args=["test_user"])
        self.assertEqual(resolve(url).func.view_class, UpdateUser)

    def test_deleteuser_url(self):
        url = reverse("delete", args=["test_user"])
        self.assertEqual(resolve(url).func.view_class, DeleteUser)
