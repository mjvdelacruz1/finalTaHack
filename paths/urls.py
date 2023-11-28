from django.urls import path, include
from . import views

app_name='paths'

urlpatterns = [
        #Leave as empty string for base url
	path('instructors/', views.instructors, name='instructors'),
	path('fields/', views.fields, name="fields"),
	path('contact/', views.contact, name="contact"),
	path('maps/', views.maps, name="maps"),
	path('login/', include('users.urls')),
    path('', views.landing, name="landing"),

]