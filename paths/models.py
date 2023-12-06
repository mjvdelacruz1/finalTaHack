from django.db import models
from cloudinary.models import CloudinaryField
from datetime import timedelta
from django.contrib.auth.models import User
from django.db.models import Avg
from django.db.models import Sum


class FieldModel(models.Model):
    FieldTitle = models.CharField(max_length=255)
    FieldDescription = models.TextField()
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')
    
    def __str__(self):
        return self.FieldTitle

class CourseModel(models.Model):                    #new
    field = models.ForeignKey(FieldModel, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='jkccejtc06k0elzgia0m')
    title = models.CharField(max_length=255)  # Add a field for the course title
    description = models.TextField()  # Add a field for the course description
    Author = models.CharField(max_length=100, default='Anonymous' )
    Rating = models.IntegerField(default=0)
    link = models.URLField(default='No link available, please report thankn you')
    created_at = models.DateTimeField(auto_now_add=True)
    
    PRICE_CHOICES = [
        ('Paid', 'Paid'),
        ('Free', 'Free'),
        ('Subscription', 'Subscription'),
        ('Paid, & Free', 'Paid, & Free'),
        ('Free, & Subscription', 'Free, & Subscription'),
        ('Paid, & Subscription', 'Paid, & Subscription'),
        ('Paid, Free, & Subscription', 'Paid, Free, & Subscription'),
    ]
    Price = models.CharField(max_length=50, choices=PRICE_CHOICES, blank=True, null=True)

    TYPE_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermidiate', 'Intermidiate'),
        ('Advanced', 'Advanced'),
    ]

    type = models.CharField(max_length=25, choices=TYPE_CHOICES, default='Major')
    
    def update_average_rating(self):
        average_rating = self.feedbackmodel_set.aggregate(Avg('rating'))['rating__avg']
        self.Rating = round(average_rating, 3) if average_rating else 0
        self.save()

    def __str__(self):
        return self.title

# class LessonModel(models.Model):        #new
#     course = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)  # Add a field for the course title
#     description = models.TextField()  # Add a field for the course description
    
#     # created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title
    

class FeedbackModel(models.Model): #feedback solely for courses
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course  = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    comment = models.TextField()
    RATE_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]

    rating = models.IntegerField(choices=RATE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.course.update_average_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.course.update_average_rating()
            
    def __str__(self):
        return self.comment


    # Add fields for your LessonModel, e.g., Lesson title, content, video link, etc.

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # Add fields specific to user profiles, e.g., user-specific settings, etc.
