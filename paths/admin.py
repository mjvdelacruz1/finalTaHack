from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
from .models import FieldModel, CourseModel, FeedbackModel

admin.site.register(FieldModel)
# admin.site.register(CourseModel)

@admin.register(CourseModel)
class CourseModelAdmin(admin.ModelAdmin):
    readonly_fields = ['Rating', 'created_at']

# admin.site.register(FeedbackModel)
@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'comment', 'rating']
    readonly_fields = ['created_at']

admin.site.unregister(Group)
