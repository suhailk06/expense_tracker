from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class Student(models.Model):
    name=models.CharField( max_length=100)
    age=models.IntegerField()
    gender=models.CharField( max_length=50,default="male")
    phone_number=models.CharField(max_length=10)
    student_bio=models.TextField()
    date_of_birth=models.DateField()
    student_registration=models.DateTimeField()
    percentage=models.FloatField()
    email=models.EmailField( max_length=254)
    
    
class Product(models.Model):
    product_name=models.CharField( max_length=50)
    slug=models.SlugField(blank=True)
    
    def save(self,*args,**kwargs)->None:
        self.slug=slugify(f"{self.product_name}")        
        return super(Product,self).save(*args,**kwargs)
    
class Contact(models.Model):
    name=models.CharField( max_length=100)
    age=models.IntegerField()
    gender=models.CharField( max_length=10)
    # ,choices=(("male","male"),("female","female"))
    comment=models.CharField(max_length=100)