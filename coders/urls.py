from django.urls import path
from . import views

app_name = "coders"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('members/', views.members, name="members"),
    path('projects/', views.projects, name="projects"),
    path('gallery/', views.gallery, name="gallery")
]
