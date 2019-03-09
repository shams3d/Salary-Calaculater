from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.employees, name='base'),
    path('base/employees_info',views.add_employee,  name='employees_info'),
    
]
