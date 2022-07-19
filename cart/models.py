from django.db import models
from customer.models import Customer
from product.models import Product


# Create your models here.


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_items = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'<Id: {self.id} Total Price: {self.total_price}>'


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    is_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return ('<Id: %d Quantity: %d Total Price: %.2f Complete: %r >' % (
                    self.id, 
                    self.quantity, 
                    self.total_price, 
                    self.is_complete))

