from django.urls import path
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('login/', views.login, name='login'),
	path('courses/', views.courses, name="courses"),
	path('roadmap/', views.roadmap, name="roadmap"),
    path('', views.landing, name="landing"),

]