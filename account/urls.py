from django.urls import path
from . import views

urlpatterns = [

    path('', views.homePage,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('portfolio/', views.portfolio,name='portfolio'),
    path('contact/', views.contact,name='contact'),
    
    path('loginpage/', views.loginPage,name='loginPage'),
    path('login/', views.auth_login,name='login'),
    path('logout/', views.logout_view,name='logout'),
    path('register/', views.register,name='register'),
    path('adminpage/', views.adminPage, name='adminPage'),
    path('student/', views.studentPage, name='studentPage'),
    path('teacher/', views.teacherPage, name='teacherPage'),
]