from django import forms
from resources.models import Resource, Note
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'tags', 'url','resource_type','difficulty','estimated_minutes','rating','technology']

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('https://'):
            raise forms.ValidationError('Your url must start with https://')
        return url

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields =['title', 'content', 'resource']
    def clean_content(self):
        content =self.cleaned_data['content']
        if len(content.strip())<10:
            raise forms.ValidationError('Content must be at least 10 characters long')
        return content.strip()



class NoteEditForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resource'].disabled = True