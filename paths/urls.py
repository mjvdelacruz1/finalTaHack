from django.urls import path, include
from . import views

app_name='paths'

urlpatterns = [
        #Leave as empty string for base url
	path('instructors/', views.instructors, name='instructors'),
	path('fields/', views.fields, name="fields"),
    path('fields/<int:field_id>/courses/', views.show_courses, name='show_courses'),

    path('courses/<int:course_id>/feedback/', views.show_feedback, name='show_feedback'),

    path('submit_feedback/<int:course_id>/', views.submit_feedback, name='submit_feedback'),
    path('feedback/success/', views.feedback_success, name='feedback_success'),
    
    # path('create/', views.field_create, name="create_field"), #new
    # path('created/', views.field_created, name='field_created'), #new
     
	path('contact/', views.contact, name="contact"),
	path('maps/', views.maps, name="maps"),
	path('login/', include('users.urls')),
    path('', views.landing, name="landing"),
]