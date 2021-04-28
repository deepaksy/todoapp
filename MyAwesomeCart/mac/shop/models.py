from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=300,default="")
    pub_date = models.DateField()
    images  = models.ImageField(upload_to='static/shop/images',default="")