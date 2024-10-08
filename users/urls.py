from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"), ### path to home page. linked to their appropriate views. When request for about page comes, it will call the views.home function
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout')
]