from django import forms
from .models import Technology, Tag
class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'description']
        labels = {'name':'Technology Name', 'description':'Technology Description'}
        widgets = {'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Technology Name'})}
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name.strip()) < 2:
            raise forms.ValidationError('The name must be at least 2 characters long')
        return name.strip()

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name',]