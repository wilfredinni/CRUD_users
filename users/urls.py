from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserList.as_view(), name="users"),
    path("new/", views.CreateUser.as_view(), name="new"),
    path("<str:slug>/", views.UserDetail.as_view(), name="profile"),
    path("delete/<str:slug>/", views.DeleteUser.as_view(), name="delete"),
    path("update/<str:slug>/", views.UpdateUser.as_view(), name="update"),
]
