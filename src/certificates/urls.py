from django.urls import path, include
from .views import certificate_generator

app_name = "certificates"

urlpatterns = [
    path("<uuid:id>/", certificate_generator, name="certificate"),
]