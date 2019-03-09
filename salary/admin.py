from django.contrib import admin
from.models import Employee
from.forms import EmployeeForm

admin.site.register(Employee)

class Employee(admin.ModelAdmin):
    readonly_fields=('salary', 'overtime')
    form = EmployeeForm

# Register your models here.
