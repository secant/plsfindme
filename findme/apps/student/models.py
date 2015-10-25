from django.db import models

class Student(models.Model):
    university = models.TextField()
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    department = models.TextField()
    course_number = models.TextField()
    course_type = models.TextField()
    section = models.IntegerField()
    bio = models.TextField()
