from django import forms
from .models import LearningPath
class LearningPathForm(forms.ModelForm):
    class Meta:
        model = LearningPath
        fields = ['title','description','difficulty','estimated_hours','resources']