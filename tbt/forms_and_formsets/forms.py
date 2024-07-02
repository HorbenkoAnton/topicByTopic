from django import forms
from .models import NewMessage,UserProfile  
from django.core.exceptions import ValidationError
import re
from datetime import date
from .models import Address  ,Image , Document
#from django.forms import modelformset_factory


class RegistrationForm(forms.Form):
    SESSION_CHOICES = [
        ('morning', 'Morning Session'),
        ('afternoon', 'Afternoon Session'),
    ]

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    preferred_session = forms.ChoiceField(choices=SESSION_CHOICES, required=True)
    additional_comments = forms.CharField(widget=forms.Textarea, required=False)
    date_of_birth = forms.DateField(
            widget=forms.DateInput(attrs={'type': 'date'}),
            input_formats=['%Y-%m-%d'])    


    def clean_email(self):
            email = self.cleaned_data['email']
            # Simulate checking for an existing email in the database
            if email == "existing@example.com":  # Replace with actual database check
                raise ValidationError("This email is already registered.")
            return email
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        pattern = re.compile(r'^\+?\d{10,15}$')
        if not pattern.match(phone_number):
            raise ValidationError("Invalid phone number format.")
        return phone_number

    def clean_date_of_birth(self):
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValidationError("You must be at least 18 years old to register.")
        return dob


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
    admin = forms.BooleanField(label='Admin', required=False)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'age', 'bio', 'admin']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get('password')
        if password:
            user.set_password(password)
        if self.cleaned_data.get('admin'):
            user.is_staff = True
            user.is_superuser = True
        if commit:
            user.save()
        return user
        
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['username', 'email', 'password','first_name', 'last_name', 'age','bio',]
        
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         password = self.cleaned_data.get('password')
#         if password:
#             user.set_password(password)
#         if commit:
#             user.save()
#         return user


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city', 'state', 'zip_code']

#AddressFormSet = modelformset_factory(Address, form=AddressForm, extra=1)


#Image training form

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['description','image']




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['description', 'file']
    
    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('.pdf'):
            raise ValidationError('Only PDF files are allowed.')
        return file
