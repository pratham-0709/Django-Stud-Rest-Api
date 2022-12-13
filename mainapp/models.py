from django.db import models

class StudentDetails(models.Model):
    name = models.CharField(max_length=50)
    mark1 = models.CharField(max_length=30)
    mark2 = models.CharField(max_length=30)
    mark3 = models.CharField(max_length=30)
    total = models.CharField(max_length=30)
