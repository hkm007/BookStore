from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    CLASS= (
        ('Premium', 'Premium'),
        ('Old', 'Old')
    )
    STATUS = (
        ('old','old'),
        ('new','new')
    )
    TAGS = (
        ('Technical','Technical'),
        ('Story','Story')
    )

    BRANCH = (
        ('ALL','ALL'),
        ('CSE','CSE'),
        ('EE','EE'),
        ('EI','EI'),
        ('ME','ME'),
        ('PE','PE'),
        ('ECE','ECE')
    )

    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_price = models.FloatField(max_length=20)
    book_author= models.CharField(max_length=100)
    book_desc= models.CharField(max_length=200)
    book_status = models.CharField(max_length=20,choices=STATUS)
    book_pic = models.ImageField(upload_to='img/',default="None Selected")
    book_date = models.DateField(max_length=20)
    book_class = models.CharField(max_length=20,choices=CLASS)
    book_branch  = models.CharField(max_length=40,choices=BRANCH,default = 'ALL')
    book_tag  = models.CharField(max_length=20,choices=TAGS,default = 'None')
    

    def __str__(self):
        return self.book_name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length = 200,default = '')
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField(max_length = 200)
    phone = models.IntegerField(default = None)
    address = models.CharField(max_length=200)
    qty = models.IntegerField(default = 1)
    total = models.FloatField(default = 0)

    def __str__(self):
        return self.book_name
