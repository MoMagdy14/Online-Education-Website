from django.db import models
import uuid
from django.utils.translation import gettext_lazy as _
from users.models import  User
from courses.models import Course

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User, related_name="certificates", on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, related_name="certificates", on_delete=models.CASCADE)
    issue_date = models.DateField(_(""), auto_now_add=True)
    