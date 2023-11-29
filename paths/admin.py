from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import FieldModel, CourseModel, LessonModel

admin.site.register(FieldModel)
admin.site.register(CourseModel)
admin.site.register(LessonModel)
admin.site.unregister(Group)
