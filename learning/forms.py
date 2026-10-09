from django import forms
from .models import LearningPath
class LearningPathForm(forms.ModelForm):
    class Meta:
        model = LearningPath
        fields = ['title','description','difficulty','estimated_hours','resources']
        labels = {'title':'Write a title','description':'Write a description','difficulty':'Choose difficulty',
                  'estimated_hours':'Choose estimated hours','resources':'Choose resources'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}),
                   'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description'}),}
        help_texts = {'title':'Please write a title','difficulty':'Please choose between  Easy, Medium,Hard',
                      'estimated_hours':'Please choose between 0.1-24 hours', 'resources':'Hold Ctrl (Cmd on Mac) to select several resources.' }
        error_messages = {'title':{'required':'Please give your Learning Path  a title'},
                         'difficulty':{'required':'Please choose difficulty'},}


    def clean_estimated_hours(self):
        estimated_hours = self.cleaned_data['estimated_hours']
        if estimated_hours <= 0:
            raise forms.ValidationError('Estimated hours cannot be less than or equal to 0')
        return estimated_hours