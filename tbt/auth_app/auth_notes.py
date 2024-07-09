# Default User Model
#already created and built in ur project provides you basic functional
# Fields
# username: A unique identifier for the user.
# password: Hashed password.
# email: Email address of the user.
# first_name: User's first name.
# last_name: User's last name.

#AbstractUser
#extends the default user model with additional fields
'''class CustomUser(AbstractUser):
    # Add any additional fields here
    phone_number = models.CharField(max_length=15, blank=True, null=True)'''


#AbstractBaseUser
#Just gives u minimum features(mostly password handling)
#used when u need define everything by yourself
'''class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

# Update settings.py
AUTH_USER_MODEL = 'myapp.CustomUser'
'''

#BaseUserManager
#provides CRUD operations for AbstractBaseUser
# As I see it, you really need that only in some really bigass  projects where everything is custom 
# and done by some programming guru who might have had Google as his side uni project.




#    '''Now let's talk about forms'''

#UserCreationForm
#as u can see used for user registration
#Fields: username, password1, password2 (password confirmation).
'''class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email',)'''

#UserChangeForm
#Used for changing user fields info from user model
'''class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')'''

#AuthenticationForm 
#It's a log in form
'''class CustomAuthenticationForm(AuthenticationForm):
    # Customization can include adding widgets or custom validation
    pass'''

#PasswordChangeForm
#Purpose: Used for changing the user's password when he remembers it
#Fields: old_password, new_password1, new_password2
'''class CustomPasswordChangeForm(PasswordChangeForm):
    # Customization can include adding widgets or custom validation
    pass'''

#PasswordResetForm
#forgot password form
#initiates reseting password

#SetPasswordForm
#Purpose: Used for setting a new password after password reset.
#Fields: new_password1, new_password2 (password confirmation).


