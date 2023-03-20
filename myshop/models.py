from django.db import models
from django.utils import timezone

import datetime

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name="Precio")
    stock = models.IntegerField(default=0, verbose_name="Stock")
    
    def __str__(self):
        return f"{self.name}"

class Order(models.Model):
    #date_time = models.DateTimeField(timezone.now())
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=200, verbose_name="Estado", default="Carrito" )
    

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cuantity = models.IntegerField(null=True, default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)