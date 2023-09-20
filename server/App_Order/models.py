from django.db import models
from App_Account.models import User


class Ingredent(models.Model):
    salad = models.IntegerField(default='0')
    cheese = models.IntegerField(default='0')
    meat = models.IntegerField(default='0')

    def __str__(self):
        return " Salad" + str(self.salad) + " Chesse " + str(self.cheese) + " Meat " + str(self.meat)


class CustomerDetail(models.Model):
    customer_address = models.TextField(blank=True)
    phone = models.CharField(max_length=30)
    payment_method = models.CharField(max_length=100)

    def __str__(self):
        return str(self.customer_address)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Ingredents = models.OneToOneField(Ingredent, on_delete=models.CASCADE , null=True)
    Customers = models.OneToOneField(CustomerDetail, on_delete=models.CASCADE ,null=True)
    price = models.CharField(max_length=10000000000, blank=False)
    ordertime = models.CharField(max_length=300,null=True,blank=True)

    def __str__(self):
        return str(self.user)
