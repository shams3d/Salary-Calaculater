from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('user','created_date','name', 'sector','grade','hrs', 'rate', 'overtime', 'salary')
       
     
        
        
         
        

        
