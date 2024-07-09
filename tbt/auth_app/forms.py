from django.contrib.auth.forms import SetPasswordForm,UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm,PasswordResetForm
from .models import CustomUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')  

class LogInForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UpdateUserInfoForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields= ('username', 'email', 'first_name', 'last_name')

class ChangePasswordForm(PasswordChangeForm):
    pass
# class CustomPasswordResetForm(PasswordResetForm):
#     pass

# class CustomSetPasswordForm(SetPasswordForm):
#     pass