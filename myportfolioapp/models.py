from django.db import models

# Create your models here.
class profile(models.Model):
    firstName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    image=models.ImageField(upload_to='upload')
    description=models.TextField()
    date=models.DateTimeField(auto_now=True)
    
    def _str_ (self):
        """Return a string representation of the model."""
        return self.firstName
    
class Product(models.Model):
    name= models.CharField(max_length=200)
    description=models.TextField()
    price=models.CharField(max_length=30)
    image=models.ImageField(upload_to='img')
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
