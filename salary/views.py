from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm
from djchoices import DjangoChoices, ChoiceItem
from django.db.models import IntegerField, CharField, F, ExpressionWrapper
def employees(request):
      employees = Employee.objects.filter(created_date__lte=timezone.now()).annotate(employee_salary=ExpressionWrapper(F('hrs') * F('rate'),output_field=IntegerField())).values_list('user', 'name','sector', 'grade', 'salary').order_by('created_date')
      employees= EmployeeForm()
      user = User
      return render(request,'salary/base.html',{'employees':employees})
def add_employee(request):
      add_employee = Employee.objects.filter(user ='2').order_by('created_date')
      add_employee = EmployeeForm()
      if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                  form = form.save(commit=False)
                  form.username = request.user
                  form.name 
                  form.sector
                  form.grade 
                  form.hrs 
                  form.rate
                  form.salary 
                  form.created_date
                  form.save()
                  return redirect(request,'employees_info')
      else:
            form = EmployeeForm()
            return render(request,'salary/employees_info.html',{'add_employee':add_employee})
           



     


