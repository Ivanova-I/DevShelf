from django.contrib import admin
from .models import Tag, Technology

class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name','description']
    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Technology, TechnologyAdmin)
class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name',)
    ordering = ('name',)

admin.site.register(Tag, TagAdmin)

# Register your models here.
