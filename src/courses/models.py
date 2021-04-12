from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

class Course(models.Model):
    name = models.CharField(_(""), max_length=80)
    course_creator = models.ForeignKey(User, related_name="courses", on_delete=models.SET_NULL, null=True)
    creation_data = models.DateField(_(""), auto_now_add=True)
    details = models.CharField(_(""), max_length=255)