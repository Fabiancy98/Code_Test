from django.db import models
from account.models import User
from suppliers.models import Supplier

# Create your models here.
class Item(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    suppliers = models.ManyToManyField('suppliers.Supplier', related_name='items')

    def __str__(self):
        return self.name