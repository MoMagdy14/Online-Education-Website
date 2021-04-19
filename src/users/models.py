from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    GENDER_CHOICES = (('male', "Male"),
              ("female", "Female"))
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    school = models.CharField(max_length=50, blank=True, null=True)
    phone = PhoneNumberField(blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, blank=True, null=True)
    graduation_state = models.CharField(max_length=50, blank=True, null=True)
    governorate = models.CharField(max_length=50, blank=True, null=True)
    graduation_year = models.CharField(max_length=50, blank=True, null=True)
    roles = models.ManyToManyField("Role", verbose_name=_("Role"), related_name="users", blank=True)
    #courses = models.ManyToManyField()
    #certifications = models.ManyToManyField()

class Role(models.Model):
    name = models.CharField(_("name") ,max_length=50)