from django.urls import path
from . import views
urlpatterns = [path('', views.resources_home, name='resources_home'),
               path('<int:pk>/', views.resources_detail, name='resources_detail'),
               path('create/', views.resources_create, name='resources_create'),
               path('<int:pk>/edit/', views.resources_edit, name='resources_edit'),
               path('<int:pk>/delete/', views.resources_delete, name='resources_delete'),
               path('notes/', views.note_home, name='note_home'),
               path('notes/<int:pk>/', views.note_detail, name='note_detail'),
               path('notes/create/', views.note_create, name='note_create'),
               path('notes/<int:pk>/edit/', views.note_edit, name='note_edit'),
               path('notes/<int:pk>/delete/', views.note_delete, name='note_delete'),
               path('<int:pk>/progress/', views.progress_update, name='progress_update')
               ]
