from django.urls import path, include
from . import views

app_name = 'users'

urlpatterns = [
        #Leave as empty string for base url
	path('login/', views.loginPage, name='loginView'),
        path('signup/', views.signup, name="signup"),
        path('logout/', views.logoutUser, name="logout"),
        

]