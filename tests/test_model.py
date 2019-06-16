from django.test import TestCase
from users.models import CustomUser


class CustomUserModel(TestCase):
    def setUp(self):
        CustomUser.objects.create_user(
            username="test_user", email="test_user@test_user.com", bio="about"
        )
        self.user = CustomUser.objects.get(username="test_user")

    def test_CustomUser_model(self):
        self.assertEqual(self.user.username, "test_user")
        self.assertEqual(self.user.email, "test_user@test_user.com")

    def test_CustomUser_model_custom_fields(self):
        self.assertEqual(self.user.bio, "about")
