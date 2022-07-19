from statistics import mode
from django.db import models

# Models for the Customer app.

class Customer(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    contact = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    comments = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return (f'<Id: {self.id} Name: {self.first_name} Contact: {self.contact}')


class Destination(models.Model):
    state = models.CharField(max_length=20)
    county = models.CharField(max_length=20)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f'<Id: {self.id} State: {self.state} Contact: {self.county}')


class Address(models.Model):
    building_name = models.CharField(max_length=50)
    building_no = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    floor = models.IntegerField(blank=True, null=True)
    street_name = models.CharField(max_length=50)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return (f'<Id: {self.id} Building Name: {self.building_name}')
