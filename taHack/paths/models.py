from django.db import models

# Create your models here.

class CourseModel(models.Model):
    CourseTitle = models.CharField(max_length=255)
    CourseDescription = models.TextField()
    Author = models.CharField(max_length=100)
    Duration = models.DurationField()  # You might want to consider using a DurationField for more flexibility
    Rating = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for currency

    def __str__(self):
        return self.CourseTitle

