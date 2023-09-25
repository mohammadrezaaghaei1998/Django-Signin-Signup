from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),
    path('custom_logout/', views.custom_logout, name='custom_logout'),

]


