from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('retreats/', views.retreats, name='retreats'),
    path('trekking/', views.trekking, name='trekking'),
    path('gallery/', views.gallery, name='gallery'),
    path('reviews/', views.reviews, name='reviews'),
    path('blogs/', views.blogs, name='blogs'),
    path('contact/', views.contact, name='contact'),
]