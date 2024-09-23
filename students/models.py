from django.db import models


# Student Model
class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    nationality = models.CharField(max_length=100)
    course_of_choice = models.CharField(max_length=255)
    program_type = models.CharField(max_length=50, choices=[('local', 'Local'), ('international', 'International')])

    def __str__(self):
        return self.name

# Course Model
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
