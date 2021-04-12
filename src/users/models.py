from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.utils.translation import gettext_lazy as _

User = settings.AUTH_USER_MODEL

class User(AbstractUser):
    GENDER_CHOICES = (('male', "Male"),
              ("female", "Female"))
    age = models.IntegerField()
    country = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    student_state = models.CharField(max_length=50)
    governorate = models.CharField(max_length=50)
    graduation_year = models.CharField(max_length=50)
    roles = models.ManyToManyField("Role", verbose_name=_("Role"), related_name="users")
    #courses = models.ManyToManyField()
    #certifications = models.ManyToManyField()

class Role(models.Model):
    name = models.CharField(_("") ,max_length=50)