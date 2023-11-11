from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class FieldModel(models.Model):
    FieldTitle = models.CharField(max_length=255)
    FieldDescription = models.TextField()
    Author = models.CharField(max_length=100)
    Duration = models.DurationField() 
    Rating = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for currency
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')

    def __str__(self):
        return self.FieldTitle
    
class CourseModel(models.Model):
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE, blank=True, null=True)
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')


class PathModel(models.Model):
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE, blank=True, null=True)

