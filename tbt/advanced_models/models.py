from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db.models import Q , F
from django.db.models import Avg ,Sum


#Abstract base classes
#I think this is good example of usage of Abstract base classes
#It can significantly shorten ur code by just defining repeating fields in one place
class BaseEmploee(models.Model):
    name = models.CharField(max_length=100)
    working_exp = models.PositiveIntegerField()
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True
class JuniourEmploee(BaseEmploee):
    mentor_name = models.CharField(max_length= 100)

class MiddleEmploee(BaseEmploee):
    list_of_projects = models.TextField()

class SeniorEmploee(BaseEmploee):
    working_exp = models.PositiveBigIntegerField()

#Multi-table inheritance
#When u need abstract class but with new table in database for every model we use Multi-table inheritance
#the only difference that we don't define meta class in these:
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ElectronicProduct(Product):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)

class BookProduct(Product):
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)

class ClothingProduct(Product):
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50)

#Custom Model Methods
#I had some missunderstanding with custom method and hooks and overriding methods 
# so they will be here as well
class Product2(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name


    #Custom methods:
    def discount_price(self):
        return self.price * (1 - self.discount /100 )
    

    #Hooks
    @receiver(pre_save, sender=Product)
    def before_product_save(sender, instance, **kwargs):
        instance.name = instance.name.upper()

    #Overided methods
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if self.discount > 50:
            raise ValueError("Discount cannot be more than 50%")
        
        # Call the original save method
        super().save(*args, **kwargs)
#######################################################################################################
'''
As I understand:
Overriding methods: Rewrites the original logic of CRUD operations.
Hooks: Adds something new to the original logic of CRUD operations without changing them. They are also bound to specific events.
Custom methods: Adds functionality beyond CRUD operations and are not bound to any events.
'''
########################################################################################################

#Complex Queries
#I had no idea what Query is so just in case:
#A query in the context of databases refers to a request for data from a database.
#Examples: .all(), .filter(), .get()

#about Queries and Querysets
#I had a problem understanding em
# But now it's ok let me explain to have a better understanding of it
#Query is a request for data to a database
#when querysets is just bunch of data from database that matches a conditions in a specific query(request)

#Q Objects
#They allow to get query with multiple conditions

products = Product.objects.filter(Q(is_on_sale=True) | Q(price__gt=100))


#F Expressions
#"F expressions in Django allow you to perform operations directly 
# on database columns without fetching the data into Python memory."
# As i undestand if we need to change a lot of data inside a database
# We don't want to fetch that data throw all cycle and lose memory stats


#Here is example without F Expression
'''products = Product.objects.all()

# Iterate over each product and update its price
for product in products:
    product.price += 0.1 * product.price  # Increase price by 10%
    product.save()  # Save the updated product back to the database'''

#Here is example with F Expression(nice short and effective :) )
'''Product.objects.update(price=F('price') * 1.1)'''


#Aggregation and Annotation
#Aggregation math operation with fields
# Sum(): Computes the sum of the values.
# Avg(): Computes the average of the values.
# Count(): Counts the number of values.
# Min(): Finds the minimum value.
# Max(): Finds the maximum value.
average_price = Product.objects.aggregate(Avg('price'))


#Annotation
#adds calculated values to each item in a queryset
products = Product.objects.annotate(discounted_price=F('price') * 0.9)
for product in products:
    print(f"{product.name}: {product.discounted_price}")


#Combine them
# Annotate each product with total sales
# Calculate the average total sales
products_with_sales = Product.objects.annotate(total_sale=Sum('order__quantity'))
average_total_sales = products_with_sales.aggregate(Avg('total_sales'))
print(average_total_sales) 

#Model Manager
#It's a model to manage another models.
#As i understand most of the time it contains some filter methods for later creation of a queryset
#or some optimization methods for example to call for Books and related Authors in one query and not
# two different queries.

class BookManager(models.Manager):
    def bestsellers(self):
        return self.filter(is_bestseller=True)
    
    
#later in view:
'''
def bestsellers_view(request):
    bestsellers = Book.objects.bestsellers()
    return render(request, 'bestsellers.html', {'bestsellers': bestsellers})
'''

#ORM I don't really know where to place this
#ORM is a technique ,I'd rather said that it's a way to write code
#That allows devs to map throw all objects in app and place em to database well orginised organized
#ORM is also strognly depends on OOP principles 