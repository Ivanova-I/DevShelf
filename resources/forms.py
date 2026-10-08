from django import forms
from resources.models import Resource, Note
class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['title', 'description', 'tags', 'url','resource_type','difficulty','estimated_minutes','rating','technology']
        labels = {'url':'Write URL', 'rating':'Write a rating', 'tags':'Choose tags', 'estimated_minutes':'Add estimated minutes'}
        help_texts = {'url':'Please write valid URL.', 'rating':'Write a rating from 0 to 5', 'tags':'Please choose at least 1', 'estimated_minutes':'Please add at least 1 min.'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
                   'url':forms.TextInput(attrs={'class':'form-control', 'placeholder':'URL'}),}
        error_messages = {'title':{'required':'Please give your Resource a title'},'url':{'required':'Please enter a link to the resource.'}}

    def clean_url(self):
        url = self.cleaned_data['url']
        if not url.startswith('https://'):
            raise forms.ValidationError('Your url must start with https://')
        return url

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields =['title', 'content', 'resource']
        labels = {'title':'Choose title', 'content':'Write your note', 'resource':'Choose related resource'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),}
        help_texts = {'content':'Write at least 10 characters', 'resource':'Please choose the resource this note is about'}
        error_messages = {'title':{'required':'Please give your Note a title'},'content':{'required':'Please write something in your note'}}
    def clean_content(self):
        content =self.cleaned_data['content']
        if len(content.strip())<10:
            raise forms.ValidationError('Content must be at least 10 characters long')
        return content.strip()



class NoteEditForm(NoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resource'].disabled = True