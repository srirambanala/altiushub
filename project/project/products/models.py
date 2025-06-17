from django.db import models

# Create your models here.

class Product(models.Model):
    location =models.CharField(max_length=50)
    rent=models.DecimalField(max_digits=10,decimal_places=2)
    bed_rooms=models.IntegerField()
    posted_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-posted_on']

    