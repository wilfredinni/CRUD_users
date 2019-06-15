from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name="users"),
    path("<str:slug>/", views.UserDetail.as_view(), name="profile"),
]
