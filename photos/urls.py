from django.urls import path
from .views import *

urlpatterns = [
    path('', Gallery, name = 'gallery'),
    path('pics/', Pics, name = 'pictures'),
    path('view/<str:pk>/', Image, name = 'picture'),
    path('add/', Add, name = 'add-photo'),
    path('about/', About, name = 'about-page'),
    path('update/<str:pk>/', PhotoUp, name = 'up-photo'),
    path('del/<str:pk>/', PhotoDel, name = 'del-photo'),
]