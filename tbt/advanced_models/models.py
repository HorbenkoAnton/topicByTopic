# from django.db import models
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from django.db.models import Q , F
# from django.db.models import Avg ,Sum
# from django.contrib.auth.models import BaseUserManager

# #Abstract base classes
# #I think this is good example of usage of Abstract base classes
# #It can significantly shorten ur code by just defining repeating fields in one place
# class BaseEmploee(models.Model):
#     name = models.CharField(max_length=100)
#     working_exp = models.PositiveIntegerField()
#     age = models.PositiveIntegerField()

#     class Meta:
#         abstract = True
# class JuniourEmploee(BaseEmploee):
#     mentor_name = models.CharField(max_length= 100)

# class MiddleEmploee(BaseEmploee):
#     list_of_projects = models.TextField()

# class SeniorEmploee(BaseEmploee):
#     working_exp = models.PositiveBigIntegerField()

# #Multi-table inheritance
# #When u need abstract class but with new table in database for every model we use Multi-table inheritance
# #the only difference that we don't define meta class in these:
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# class ElectronicProduct(Product):
#     brand = models.CharField(max_length=50)
#     model = models.CharField(max_length=50)

# class BookProduct(Product):
#     author = models.CharField(max_length=100)
#     isbn = models.CharField(max_length=13)

# class ClothingProduct(Product):
#     size = models.CharField(max_length=10)
#     color = models.CharField(max_length=50)

# #Custom Model Methods
# #I had some missunderstanding with custom method and hooks and overriding methods 
# # so they will be here as well
# class Product2(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

#     def __str__(self):
#         return self.name


#     #Custom methods:
#     def discount_price(self):
#         return self.price * (1 - self.discount /100 )
    

#     #Hooks
#     @receiver(pre_save, sender=Product)
#     def before_product_save(sender, instance, **kwargs):
#         instance.name = instance.name.upper()

#     #Overided methods
#     def save(self, *args, **kwargs):
#         self.name = self.name.lower()
#         if self.discount > 50:
#             raise ValueError("Discount cannot be more than 50%")
        
#         # Call the original save method
#         super().save(*args, **kwargs)
# #######################################################################################################
# '''
# As I understand:
# Overriding methods: Rewrites the original logic of CRUD operations.
# Hooks: Adds something new to the original logic of CRUD operations without changing them. They are also bound to specific events.
# Custom methods: Adds functionality beyond CRUD operations and are not bound to any events.
# '''
# ########################################################################################################

# #Complex Queries
# #I had no idea what Query is so just in case:
# #A query in the context of databases refers to a request for data from a database.
# #Examples: .all(), .filter(), .get()

# #about Queries and Querysets
# #I had a problem understanding em
# # But now it's ok let me explain to have a better understanding of it
# #Query is a request for data to a database
# #when querysets is just bunch of data from database that matches a conditions in a specific query(request)

# #Q Objects
# #They allow to get query with multiple conditions

# products = Product.objects.filter(Q(is_on_sale=True) | Q(price__gt=100))


# #F Expressions
# #"F expressions in Django allow you to perform operations directly 
# # on database columns without fetching the data into Python memory."
# # As i undestand if we need to change a lot of data inside a database
# # We don't want to fetch that data throw all cycle and lose memory stats


# #Here is example without F Expression
# '''products = Product.objects.all()

# # Iterate over each product and update its price
# for product in products:
#     product.price += 0.1 * product.price  # Increase price by 10%
#     product.save()  # Save the updated product back to the database'''

# #Here is example with F Expression(nice short and effective :) )
# '''Product.objects.update(price=F('price') * 1.1)'''


# #Aggregation and Annotation

# #Aggregation math operation with fields
# # Sum(): Computes the sum of the values.
# # Avg(): Computes the average of the values.
# # Count(): Counts the number of values.
# # Min(): Finds the minimum value.
# # Max(): Finds the maximum value.
# average_price = Product.objects.aggregate(Avg('price'))


# #Annotation
# #adds calculated values to each item in a queryset
# products = Product.objects.annotate(discounted_price=F('price') * 0.9)
# for product in products:
#     print(f"{product.name}: {product.discounted_price}")


# #Combine them
# # Annotate each product with total sales
# # Calculate the average total sales
# products_with_sales = Product.objects.annotate(total_sale=Sum('order__quantity'))
# average_total_sales = products_with_sales.aggregate(Avg('total_sales'))
# print(average_total_sales) 

# #Model Manager
# #It's a model to manage another models.
# #As i understand most of the time it contains some filter methods for later creation of a queryset
# #or some optimization methods for example to call for Books and related Authors in one query and not
# # two different queries.

# class BookManager(models.Manager):
#     def bestsellers(self):
#         return self.filter(is_bestseller=True)
    
    
# #later in view:
# '''
# def bestsellers_view(request):
#     bestsellers = Book.objects.bestsellers()
#     return render(request, 'bestsellers.html', {'bestsellers': bestsellers})
# '''

# #ORM I don't really know where to place this
# #ORM is a technique ,I'd rather said that it's a way to write code
# #That allows devs to map throw all objects in app and place em to database well organized
# #ORM is also strognly depends on OOP principles 

# #abstact user
# #Class used to create a custom user models
# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     age = models.IntegerField(blank=True, null=True)
#     #u can set parametrs with this two:
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#     #if we changing username field we need to override get_username() method
#     def get_username(self):
#         return self.email

# #Here is list of all default fields of AbstractUser
# #U can choose one u need in ur form class
# '''
# username: A unique identifier for the user. This is typically used for authentication purposes.
# password: The hashed password for the user account.
# email: An email address associated with the user account. This is often used for communication and as an alternative identifier.
# first_name: The first name of the user.
# last_name: The last name of the user.
# is_active: A boolean field indicating whether the user account is active or not. Inactive accounts may be prevented from logging in.
# is_staff: A boolean field indicating whether the user is a staff member. Staff members may have additional permissions or privileges.
# is_superuser: A boolean field indicating whether the user has superuser/administrator privileges. Superusers have full access to the Django admin interface and can perform administrative tasks.
# '''

# #AbstractBaseUser
# # provides minimal functionality, requiring you to define
# # all the fields and methods required for user authentication and management.
# #requires you to define authentication-related methods such as 

# #BaseUserManager
# #Is like ModelManager for AbstactBaseUsers there defined and overrided methods if needed
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.db import models

# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('The Email field must be set')
#         user = self.model(email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     #Here we also can define method for creating admin user

# class CustomUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(default=True)

#     objects = CustomUserManager()
#     #we also can use parametrs with these
#     USERNAME_FIELD = 'email'

#     def __str__(self):
#         return self.email



# #AUTH_USER_MODEL 
# # settings.py

# AUTH_USER_MODEL = 'myapp.CustomUser'
# '''Replace 'myapp.CustomUser' with the path to your custom user model. 
# This ensures that Django's authentication system uses your custom user model throughout the project.'''


# #i was revising some info and I understood that i missed field relations
# # so there is an quick example to see how it works
# # there are 3 types of field relations: OneToOne, ForeignKey(one to many) , ManyToMany
# from django.db import models
# from django.contrib.auth.models import AbstractUser


# #Here we create custom usermodel
# class UserProfile(AbstractUser):
#     age = models.IntegerField(blank=True, null=True)
#     bio = models.TextField(blank=True)


# #We create a model for a school
# class School(models.Model):
#     name = models.CharField(max_length=100)
#     address = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# #We bind a object of user and school to principal 
# #so in database every principal would have field with id of a school and a user
# class Principal(models.Model):
#     user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
#     school = models.OneToOneField(School, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.get_full_name()} ({self.school.name})'
# #here we bind teacher to a school so every school can have multiple teachers
# # (one school many teacher)
# class Teacher(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.get_full_name()} ({self.school.name})'

# #Here we bind course to a school so school could have many courses
# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.name


# #Here we bind a student to a many courses(many studets may have many courses)
# #and also every school can have many students
# class Student(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     courses = models.ManyToManyField(Course)
#     school = models.ForeignKey(School, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.user.get_full_name()
