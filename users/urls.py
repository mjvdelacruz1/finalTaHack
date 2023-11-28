from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
        #Leave as empty string for base url
	path('login/', views.loginPage, name='login'),
        path('signup/', views.signup, name="signup"),

]