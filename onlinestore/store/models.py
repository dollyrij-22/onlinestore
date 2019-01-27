from django.db import models
from enum import Enum

class OrderStatus(Enum):
    PL = 'PLACED'
    AA = 'AGENT_ASSIGNED'
    DL = 'DELIVERED'

# Create your models here.

class Store(models.Model):
    name = models.CharField(max_length = 250,null=False)
    address = models.CharField(max_length = 250,null=False)
    contact = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=False)

class Agent(models.Model):
    name = models.CharField(max_length=250, null=False)
    contact = models.IntegerField(null=False)
    is_available = models.SmallIntegerField(default=1,null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    is_deleted = models.SmallIntegerField(default=0,null=False)

class Customer(models.Model):
    name = models.CharField(max_length=250, null=False)
    contact = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    is_deleted = models.SmallIntegerField(default=0, null=False)

class Product(models.Model):
    name = models.CharField(max_length=250, null=False)
    price = models.FloatField(null=False)
    store_id = models.ForeignKey(Store,models.CASCADE)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)

class CustomerAddress(models.Model):
    customer_id = models.ForeignKey(Customer,models.CASCADE)
    address = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(null=False)

class Order(models.Model):
    agent_id = models.ForeignKey(Agent,models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer,models.DO_NOTHING)
    delivery_address = models.CharField(max_length=250,null=False)
    delivery_time = models.DateTimeField(null=False)
    staus = models.CharField(max_length=250,choices=[(tag, tag.value) for tag in OrderStatus],default=OrderStatus.PL)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    created_at = models.DateTimeField(null=False)
    updated_at = models.DateTimeField(null=True)
    is_deleted = models.SmallIntegerField(default=0, null=False)

class OrderProduct(models.Model):
    quantity = models.IntegerField(null=False)
    cost_per_item = models.FloatField(null=False)
    order_id = models.ForeignKey(Order,models.DO_NOTHING)
    product_id = models.ForeignKey(Product,models.DO_NOTHING)

