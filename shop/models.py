from django.db import models

# Create your models here.

class Product(models.Model):
    id=models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shop/images')
    category =models.CharField(max_length=50 , default="")
    pub_data=models.DateField()

    def __str__(self):
        return self.name



class Contact(models.Model):
    mess_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    Phone = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self) :
        return self.name
    
class Registration(models.Model):
    ID=models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, default="")
    Phone = models.CharField(max_length=100, default="")
    address = models.CharField(max_length=500, default="")
    password=models.CharField(max_length=100,default="")
    cpassword = models.CharField(max_length=100,default="")
    gender = models.CharField(max_length=500, default="")
    Country = models.CharField(max_length=500, default="")
    

    def __str__(self) :
        return self.name
