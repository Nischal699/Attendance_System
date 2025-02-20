from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    path('', views.homePage,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('portfolio/', views.portfolio,name='portfolio'),
    
    
    path("account/", include("account.urls")),  # Assuming an account app exists
    path("contactenquiry/", include("contactenquiry.urls")),  # Assuming a contactenquiry app exists
]
