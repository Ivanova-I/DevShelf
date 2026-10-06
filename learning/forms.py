from django import forms
from .models import LearningPath
class LearningPathForm(forms.ModelForm):
    class Meta:
        model = LearningPath
        fields = ['title','description','difficulty','estimated_hours','resources']

    def clean_estimated_hours(self):
        estimated_hours = self.cleaned_data['estimated_hours']
        if estimated_hours <= 0:
            raise forms.ValidationError('Estimated hours cannot be less than or equal to 0')
        return estimated_hours