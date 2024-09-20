from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-website/', views.add_website, name='add_website'),
    path('add-website-configuration/', views.add_website_configuration, name='add_website_config'),
]