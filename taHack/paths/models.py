from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class CourseModel(models.Model):
    CourseTitle = models.CharField(max_length=255)
    CourseDescription = models.TextField()
    Author = models.CharField(max_length=100)
    Duration = models.DurationField() 
    Rating = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for currency
    image = CloudinaryField('image', default='taHack\static\images\PLACEHOLDER_NULL.png')


    def __str__(self):
        return self.CourseTitle

