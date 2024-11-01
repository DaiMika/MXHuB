from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=255, default="MXHuB Learning Platform")
    description = models.TextField(default="A platform for immersive learning experiences.")
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.title

class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=255, default="Introduction to Python")
    content = models.TextField(default="Learn the basics of Python programming.")

    def __str__(self):
        return f"{self.title} - {self.course.title}"

class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="quizzes")
    question = models.CharField(max_length=255, default="What is Python?")
    answer = models.CharField(max_length=255, default="A programming language.")

    def __str__(self):
        return f"Quiz for {self.module.title}: {self.question}"

