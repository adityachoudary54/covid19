from django import forms
from .models import Notes
# from django.contrib.auth.models import User
class notesForm(forms.ModelForm):
    createdDate=forms.DateTimeField()
    modifiedDate=forms.DateTimeField()
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'style': 'border-color: blue;',
                'placeholder': 'Write your title here',
                'class':'form-control'
            }
        )
    )
    content = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Write your content here',
                'style': 'border-color: orange;',
                'class':'form-control'
            }),
    )
    class Meta:
        model=Notes
        fields=[
            'title',
            'content',
            'createdDate',
            'modifiedDate'
        ]

class userForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'name':'username','class':'form-control'}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={'name':'password','class':'form-control'}))
