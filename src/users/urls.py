from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import Register

app_name = "users"
urlpatterns = [
    path("login/", TokenObtainPairView.as_view() , name="login"),
    path("register/", Register.as_view(), name="register"),

]