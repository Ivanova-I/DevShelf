from django.contrib import admin
from .models import Resource,Note
class ResourceAdmin(admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ['title','resource_type','difficulty','technology','rating']
    list_filter = ['resource_type','difficulty','technology','rating']
    ordering = ['title','-created_at']

admin.site.register(Resource, ResourceAdmin)
class NoteAdmin(admin.ModelAdmin):
    search_fields = ['title','content']
    list_display = ['title','resource','created_at']
    ordering = ['-created_at']

admin.site.register(Note, NoteAdmin)

# Register your models here.
