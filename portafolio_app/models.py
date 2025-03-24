from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    git_link = models.URLField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
