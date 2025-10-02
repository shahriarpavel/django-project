from django.urls import path
from .views import home_view, login_view, signup_view, logout_view, profile_view

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("signup/", signup_view, name="signup"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_view, name="profile"),

]
