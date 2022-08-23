from django.contrib import admin
from .models import (
    Customer,
    Destination,
    Address
)


# Register your models here.
admin.site.register(Customer)
admin.site.register(Destination)
admin.site.register(Address)
