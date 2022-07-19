from unicodedata import category, name
from django.db import models

# Models for the Product App.


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self) -> str:
        return (f'<Id: {self.id} Name: {self.name}')



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    image_path = models.TextField()

    def __str__(self) -> str:
        return (f'<Id: {self.id} Name: {self.title} Price: {self.price}')
