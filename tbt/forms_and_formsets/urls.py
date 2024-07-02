from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('new_message/', views.new_message_view,name='new_message'),
    path('auth/', views.user_profile_view, name='auth'),
    path('register/', views.register, name='register'),
    path('manage_addresses/', views.manage_addresses, name='manage_addresses'),
    path('upload/', views.upload_image, name='upload_image'),
    path('images/', views.images_list, name='images_list'),
    path('docs/', views.upload_file, name='upload_file'),   
] 
