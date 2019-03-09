from django import forms
from .models import Employee
from django.db.models import IntegerField, CharField, F, ExpressionWrapper

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('user','created_date','name', 'sector','grade','hrs', 'rate', 'salary')
       
     
        
        
         
        

        
