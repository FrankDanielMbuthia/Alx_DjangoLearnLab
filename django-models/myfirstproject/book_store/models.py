from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    published_date = models.DateField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
