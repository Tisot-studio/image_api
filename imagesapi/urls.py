from django.urls import path 
from . import views


urlpatterns = [
    path('images/', views.getImages, name='get-all-images'),
    path ('images/<str:pk>/resize/', views.resizeImage, name='resize-image'),
    path ('images/<str:pk>/', views.getImage, name='get-image'), 
]