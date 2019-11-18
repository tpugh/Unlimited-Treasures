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
