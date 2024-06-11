from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', include('forms_and_formsets.urls')),
]
