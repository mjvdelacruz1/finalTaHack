from django.db import models
from cloudinary.models import CloudinaryField

from django.db import models
from cloudinary.models import CloudinaryField

class FieldModel(models.Model):
    FieldTitle = models.CharField(max_length=255)
    FieldDescription = models.TextField()
    Author = models.CharField(max_length=100)
    Duration = models.DurationField()
    Rating = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')
    
    def __str__(self):
        return self.FieldTitle

class CourseModel(models.Model):                    #new
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')
    title = models.CharField(max_length=255)  # Add a field for the course title
    description = models.TextField()  # Add a field for the course description

    def __str__(self):
        return self.title

class LessonModel(models.Model):        #new
    course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)  # Add a field for the course title
    description = models.TextField()  # Add a field for the course description

    def __str__(self):
        return self.title
    # Add fields for your LessonModel, e.g., Lesson title, content, video link, etc.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add fields specific to user profiles, e.g., user-specific settings, etc.
