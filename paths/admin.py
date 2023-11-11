from django.contrib import admin

# Register your models here.
from .models import FieldModel, CourseModel, LessonModel

admin.site.register(FieldModel)
admin.site.register(CourseModel)
admin.site.register(LessonModel)
