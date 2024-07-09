from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_user_info, name='update_info'),
    path('profile/change-password/', views.change_password, name='change_password'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]
