from django.db import models

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
    CATEGORY = (
        ('Technical','Technical'),
        ('Story','Story')
    )

    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=30)
    book_price = models.FloatField(max_length=30)
    book_author= models.CharField(max_length=30)
    book_desc= models.CharField(max_length=30)
    book_status = models.CharField(max_length=30,choices=STATUS)
    book_pic = models.ImageField(upload_to='img/',default="None Selected")
    book_date = models.DateField(max_length=30)
    book_class = models.CharField(max_length=30,choices=CLASS)
    book_category  = models.CharField(max_length=30,choices=CATEGORY)

    def __str__(self):
        return self.book_name