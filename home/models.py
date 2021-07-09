from django.db import models
from django.utils import timezone
# Create your models here.
class Prdlist(models.Model):
    product= models.CharField(max_length=100)
    brand= models.CharField(max_length=100)
    brand_pd= models.CharField(max_length=100)
    pd_details= models.CharField(max_length=500)
    price= models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    stock = models.IntegerField(max_length=500)


class Add_info(models.Model):
    username =models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    location=models.CharField(max_length=100)


class Transact(models.Model):
    username =models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    product= models.CharField(max_length=100)
    brand= models.CharField(max_length=100)
    brand_pd= models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    review_given=models.BooleanField(default=False)
    Quantity = models.CharField(max_length=100)
    Total_Price= models.CharField(max_length=100)


class Review(models.Model):
    username =models.CharField(max_length=100)
    review=models.CharField(max_length=700)
    brand_pd=models.CharField(max_length=100)
    review_analysis=models.CharField(max_length=100)
    enquired =models.BooleanField(default=False)

class Cart(models.Model):
    username =models.CharField(max_length=100)
    product= models.CharField(max_length=100)
    brand= models.CharField(max_length=100)
    brand_pd= models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    Quantity = models.CharField(max_length=100)
    Total_Price= models.IntegerField(max_length=500)
    price= models.CharField(max_length=100)
    sold= models.BooleanField(default=False)



    

