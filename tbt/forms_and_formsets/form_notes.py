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

# Form Types
# (forms.Form, forms.ModelForm, UserCreationForm, 
# UserChangeForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm)


# forms.Form:
# A basic form class for custom forms.
# Use when you need complete control over form fields and validation.

# forms.ModelForm:
# A form that is tied to a Django model.
# Automatically generates form fields from model fields.
# Use when you need a form to create or update a model instance.

# UserCreationForm:
# A form that provides fields for creating a new user, including password fields.
# Automatically handles password hashing.
# Extends forms.ModelForm.

# UserChangeForm:
# A form for updating user information.
# Excludes password fields by default.
# Extends forms.ModelForm.

# AuthenticationForm:
# A form for handling user authentication (login).
# Includes fields for username and password.

# PasswordChangeForm:
# A form for allowing users to change their password.
# Includes fields for old password, new password, and password confirmation.

# PasswordResetForm:
# A form for initiating a password reset.
# Includes a field for entering an email address.

# SetPasswordForm:
# A form for setting a new password without entering the old password.
# Used in password reset workflows.


'''FORMSETS'''
#helps to write multiple connected forms
from .models import Address
from .forms import AddressForm
from django.forms import modelformset_factory
AddressFormSet = modelformset_factory(Address, form=AddressForm, extra=1)

#Here how u deal with it in view:
# if request.method == 'POST':
#         formset = AddressFormSet(request.POST, queryset=Address.objects.filter(user=user))
#         if formset.is_valid():
#             addresses = formset.save(commit=False)
#             for address in addresses:
#                 address.user = user
#                 address.save()
#             return redirect('success_page')  # Redirect to success page upon successful form submission
#     else:
#         formset = AddressFormSet(queryset=Address.objects.filter(user=user))

#U need to get all forms ( addresses = formset.save(commit=False) )
# and then loop throw them and .save() them individualy 

#U can add custom validation on different lvls:
#Field, Form and Formset lvls, by using "clean" methods.
#on Field lvl we use new custom clean_method
#on form and Formset lvl we overide existing one