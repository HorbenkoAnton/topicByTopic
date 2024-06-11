from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.contact_view, name='contact'),
    path('new_message', views.new_message_view,name='new_message')
]
