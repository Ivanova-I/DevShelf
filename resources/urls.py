from django.urls import path
from . import views
urlpatterns = [path('', views.resources_home, name='resources_home'),
               path('<int:pk>/', views.resources_detail, name='resources_detail'),
               path('create/', views.resources_create, name='resources_create'),
               path('<int:pk>/edit/', views.resources_edit, name='resources_edit'),
               path('<int:pk>/delete/', views.resources_delete, name='resources_delete'),]
