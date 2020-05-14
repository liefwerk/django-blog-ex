from django.urls import path
# we import the view
from . import views

# there we store our urls
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
