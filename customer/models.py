from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    comments = models.CharField()

    def __str__(self) -> str:
        return (f'<Id: {self.id} Name: {self.first_name} Contact: {self.contact}')



