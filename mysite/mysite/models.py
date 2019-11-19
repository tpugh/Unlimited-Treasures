"""
http://www.learningaboutelectronics.com/Articles/How-to-create-a-database-table-in-Django.php
1. add class
2. python manage.py makemigrations [AppName]
3. python manage.py migrate
Example
class Students(models.Model):
    firstname= models.CharField(max_length=100)
    lastname= models.CharField(max_length=100)
    email= models.CharField(max_length=200)
"""
from django.db import models
from mysite.credit import CreditCardField

class Customer(models.Model):
    email = models.CharField(max_length=200, primary_key=True)
    fname = models.CharField(max_length=100)
    lanme = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    password = models.CharField(max_length=50)
    phone_number = models.CharField('Contact PHone', max_length=20)
    default_credit_card = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=12, max_length=19)

class OnlineStore(models.Model):
    web_address = models.CharField(max_length=200, primary_key=True) 
    email = models.CharField(max_length=200)

class Products(models.Model):
    product_id = models.CharField(max_length=200, primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)  

class Cart(models.Model):
    cart_id = models.CharField(max_length=100, primary_key=True)
    delivery_address = models.CharField(max_length=300)
    
class Payment(models.Model):
    payment_no = models.CharField(max_length=10, primary_key=True)
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)
    email = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Orders(models.Model):
    cart_id = models.ForeignKey(Cart, on_delete=models.CASCADE)