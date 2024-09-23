from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-website/', views.add_website, name='add_website'),
    path('add-website-configuration/<int:website_id>/', views.add_website_configuration, name='add_website_config'),
    path('api/search/', views.search_by_url, name='search_by_url'),
]