from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('instructors/', views.instructors, name='instructors'),
	path('courses/', views.courses, name="courses"),
	path('contact/', views.contact, name="contact"),
	path('maps/', views.maps, name="maps"),
    path('', views.landing, name="landing"),

]