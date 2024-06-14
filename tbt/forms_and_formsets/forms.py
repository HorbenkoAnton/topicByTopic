from django import forms
from .models import NewMessage,UserProfile  

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

        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'first_name', 'last_name', 'age','bio']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
