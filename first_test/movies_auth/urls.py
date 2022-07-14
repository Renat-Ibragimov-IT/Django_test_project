from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path("signup/", views.sign_up_user, name="signup"),
    path("login/", views.LoginUser.as_view(), name="login")
]
