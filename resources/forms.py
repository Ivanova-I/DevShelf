from django import forms
from resources.models import Resource
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'tags', 'url','resource_type','difficulty','estimated_minutes','rating','technology']
