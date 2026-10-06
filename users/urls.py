from django.urls import path

from users.views import *

urlpatterns = [
    path("", LoginView.as_view({"get":"login_fun","post":"login_fun"}), name="users-login"),
    path("login/", LoginView.as_view({"get":"login_fun","post":"login_fun"}), name="users-login"),
    path("register/", RegisterView.as_view({"get":"register_fun","post":"register_fun"}), name="users-register"),
    path("dashboard/", DashboardView.as_view({"get":"dashboard_fun","post":"dashboard_fun"}), name="users-dashboard"),
    path("logout/", LogoutView.as_view({"get":"logout_fun","post":"logout_fun"}), name="users-logout"),
]