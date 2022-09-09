from unicodedata import name
from django.db import models

# Create your models here.


class Contact(models.Model):

    SKILL_CHOICES = (
        ('Beginner', 'BEGINNER'),
        ('Intermediate', 'INTERMEDIATE'),
        ('Pro', 'PRO'),
    )

    name = models.CharField(max_length=100)
    rollno = models.TextField(primary_key=True, unique=True)
    mail = models.EmailField()
    skill = models.CharField(
        max_length=15, choices=SKILL_CHOICES, default='Beginner')

    def __str__(self):

        return self.name


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
