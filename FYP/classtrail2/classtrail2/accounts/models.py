from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):

    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_name = models.CharField(max_length=100)
    teacher_id = models.CharField(max_length=20, default='000')

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, default='000')


class Classroom(models.Model):
    class_id = models.CharField(max_length = 5, default = '00000')
    subject_name = models.CharField(max_length=100)
    code = models.CharField(max_length = 5, default = '00000')
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, primary_key='false')
    students = models.ManyToManyField(Student, on_delete=models.CASCADE, primary_key='false')
