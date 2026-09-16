from django.contrib import admin
from .models import LearningPath
class LearningPathAdmin(admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ('title','difficulty','estimated_hours','created_at')
    list_filter = ('difficulty',)
    ordering = ('-created_at',)
admin.site.register(LearningPath,LearningPathAdmin)


