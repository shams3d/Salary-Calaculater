from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    path('',views.employee_list, name='employee_list'),
    path('employee/<int:pk>/',views.employee_details,name='employee_detail'),
    path('employee/new',views.add_employee,  name='new_employee'),
    path('employee/<int:pk>/edit/', views.edit_employee, name='edit_employee'),
   
   
    
    
]
