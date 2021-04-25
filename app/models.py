from django.db import models
from django.contrib.auth.models import User
import datetime

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email   = models.CharField(max_length=30)
    date   =   models.DateField()
    def __str__(self):
    	return self.first_name
       

class Post(models.Model):
  
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = models.TextField(max_length=2000)
    picture = models.FileField(upload_to="post/")
    def __str__(self):
    	return self.title
class register33(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    emailid = models.CharField(max_length=30,null=True)
    username = models.CharField(max_length=30,unique=True,null=True)
    password = models.CharField(max_length=30,null=True)
    date   =   models.DateField()
    picture = models.FileField(upload_to="post/",null=True)
    contact_number = models.IntegerField(null=True)
    Address = models.TextField(max_length=50,null=True)
    def __str__(self):
        return self.Firstname
class Category(models.Model):
    cat_name = models.CharField(max_length=30)
    cover_pic = models.FileField(upload_to="post/",null=True)
    
    def __str__(self):
        return self.cat_name                        

class ArtistAccount(models.Model):
    user_id = models.ForeignKey(register33, on_delete=models.CASCADE,null=True)
    productname = models.CharField(max_length=30,null=True)
    image = models.FileField(upload_to="post/",null=True)
    productprice = models.FloatField(null=True)
    saleprice = models.FloatField(max_length=30,null=True)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    content = models.TextField(max_length=2000,null=True)
    height = models.IntegerField(null=True)
    width = models.IntegerField(null=True)
    def __str__(self):
        return self.content

class cart(models.Model):
    user =models.ForeignKey(register33,on_delete = models.CASCADE)
    product = models.ForeignKey(ArtistAccount,on_delete = models.CASCADE)
    quantity = models.IntegerField()
    status = models.BooleanField(default=False)
    added_on =models.DateTimeField(auto_now_add=True,null=True)
    update_on = models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return self.user.username

class Order(models.Model):
    cust_id = models.ForeignKey(register33,on_delete=models.CASCADE)
    cart_ids = models.CharField(max_length=250)
    product_ids = models.CharField(max_length=250)
    invoice_id = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    processed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cust_id.username 

class Photo(models.Model):
    user_id  = models.ForeignKey(register33,on_delete = models.CASCADE) 
    photo = models.FileField(upload_to="post/",null=True)
    Amount = models.IntegerField(null=True)

    def __str__(self):
        return self.user_id.username
   

class Customphoto(models.Model):
    user_id  = models.ForeignKey(register33,on_delete = models.CASCADE) 
    photo = models.FileField(upload_to="post/",null=True)
    Imageheight = models.IntegerField(null=True)
    ImageWidth = models.IntegerField(null=True) 
    Category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.username 

class Selleraccount(models.Model):
    
    shop = models.CharField(max_length=30,null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    contact_number = models.IntegerField(null=True)
    shopaddress = models.TextField(max_length=250,null=True)

    def __str__(self):
        return self.user.username                            