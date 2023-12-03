from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import FieldModel, CourseModel, LessonModel, FeedbackModel

admin.site.register(FieldModel)
# admin.site.register(CourseModel)

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    readonly_fields = ['Rating']

admin.site.register(LessonModel)

# admin.site.register(FeedbackModel)
@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'comment', 'rating']
    readonly_fields = ['created_at']

admin.site.unregister(Group)
