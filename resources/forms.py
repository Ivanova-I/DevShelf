from django import forms
from resources.models import Resource, Note
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'tags', 'url','resource_type','difficulty','estimated_minutes','rating','technology']

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields =['title', 'content', 'resource']


class NoteEditForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resource'].disabled = True