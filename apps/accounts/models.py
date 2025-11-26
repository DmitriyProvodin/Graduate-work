from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
class Role(models.TextChoices):
ADMIN = 'admin', 'Admin'
TEACHER = 'teacher', 'Teacher'
STUDENT = 'student', 'Student'


role = models.CharField(max_length=20, choices=Role.choices, default=Role.STUDENT)


def is_teacher(self):
return self.role == self.Role.TEACHER


def is_student(self):
return self.role == self.Role.STUDENT