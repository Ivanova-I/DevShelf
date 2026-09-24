from django.urls import path
from . import views
urlpatterns = [
    path('', views.catalog_home, name='catalog_home'),
    path('technologies/<int:pk>/', views.technology_detail, name='technology_detail'),
    path('technologies/create/', views.technology_create, name='technology_create'),
    path('technologies/<int:pk>/edit/', views.technology_edit, name='technology_edit'),
    path('technologies/<int:pk>/delete/', views.technology_delete, name='technology_delete'),
    path('tags/', views.tag_home, name='tag_home'),
    path('tags/create/', views.tag_create, name='tag_create'),
    path('tags/<int:pk>/edit/', views.tag_edit, name='tag_edit'),
    path('tags/<int:pk>/delete/', views.tag_delete, name='tag_delete'),
]