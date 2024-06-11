from django import forms
from .models import NewMessage  

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class NewMessageForm(forms.ModelForm):
    class Meta:
        model = NewMessage
        fields = ['subject', 'content', 'sender']
        widgets = {
            'content': forms.Textarea
        }
