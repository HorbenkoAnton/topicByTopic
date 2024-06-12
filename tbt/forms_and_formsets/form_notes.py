from django import forms
from .models import NewMessage  

#Form is a dataset of user input. It's like a bridge between user and backend logic

#forms.Form vs forms.ModelForm

#forms.Form is manualy created and used for better control and validation
#and yeah they are independent of a django model
'''DATA FROM forms.Form IS NOT STORED IN DATABASE'''
class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

#forms.ModelForm us automatically created for a Django model it faster to write and gives less control
'''DATA FROM forms.ModelForm IS AUTOMATICALLY STORED IN DATABASE(cause it binded to a model)'''
class NewMessageForm(forms.ModelForm):
    class Meta:
        model = NewMessage
        fields = ['subject', 'content', 'sender']
        widgets = {
            'content': forms.Textarea
        }

# I don't really understand why we need a forms.Form cause most of times 
# we want data from form be saved in database.
# so why we need form.Form with more control over validation if we can't save data with it 

#I  understand it's good for non-database tasks but i just can't imagine one