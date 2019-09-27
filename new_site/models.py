from django.db import models

class Car(models.Model):
    model=models.CharField(max_length=40)
