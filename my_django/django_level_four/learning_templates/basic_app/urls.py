from django.urls import path, include
from basic_app import views

app_name = "basic_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
]