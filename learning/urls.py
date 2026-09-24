from django.urls import path
from . import views
urlpatterns = [path('', views.learning_home, name='learning_home'),
               path('<int:pk>/', views.learning_detail, name='learning_detail'),
               path('create/', views.learning_create, name='learning_create'),
               path('<int:pk>/edit/', views.learning_edit, name='learning_edit'),
               path('<int:pk>/delete/', views.learning_delete, name='learning_delete'),]