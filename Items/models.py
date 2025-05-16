from django.db import models

# Create your models here.

class Good(models.Model):
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    description = models.TextField()
    # the upload to attribute items is telling django to create a folder where images in which will be posted will be kept this is deffernt from the image folder in your static
    image = models.ImageField(upload_to='items')
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
