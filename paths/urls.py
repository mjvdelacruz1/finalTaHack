from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('instructors/', views.instructors, name='instructors'),
	path('fields/', views.fields, name="fields"),
    path('fields/<int:field_id>/courses/', views.show_courses, name='show_courses'),
	path('contact/', views.contact, name="contact"),
	path('maps/', views.maps, name="maps"),
	path('login/', views.login, name="login"),
	path('signup/', views.signup, name="signup"),
 
    path('', views.landing, name="landing"),

]