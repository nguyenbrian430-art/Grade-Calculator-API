from django.db import models
# from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

class Class(models.Model):
    className=models.CharField(max_length=50)

class Assignment(models.Model):
    className=models.ForeignKey(Class, on_delete=models.CASCADE)
    # user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    grade=models.FloatField(validators=[MinValueValidator(0)])
