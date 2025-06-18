from django.urls import path
from .views import index, create

urlpatterns = [
    path('', index, name='index'),  # Home page
    path('create/', create, name='create'),  # Create user page
]