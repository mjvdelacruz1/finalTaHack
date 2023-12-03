from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import FieldModel, CourseModel, LessonModel, FeedbackModel

admin.site.register(FieldModel)
admin.site.register(CourseModel)
admin.site.register(LessonModel)
admin.site.register(FeedbackModel)
admin.site.unregister(Group)
