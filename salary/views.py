from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from .models import Employee
from .forms import EmployeeForm
from djchoices import DjangoChoices, ChoiceItem
from django.db.models import IntegerField, CharField, F, ExpressionWrapper

def employee_list(request):
      employees=Employee.objects.filter(user= '2').order_by('-published_date')
      return render(request,'salary/employee_list.html',{'employees':employees})
def employee_details(request,pk):
      employee = get_object_or_404(Employee, pk=pk)
      return render(request, 'salary/employee_detail.html', {'employee': employee})
def add_employee(request):
      employee = EmployeeForm()
      if request.method == "POST":
            form = EmployeeForm(request.POST)
            if form.is_valid():
                  employee = form.save(commit=False)
                  employee.username = request.user
                  employee.name 
                  employee.sector
                  employee.grade 
                  employee.hrs 
                  employee.rate
                  employee.salary 
                  employee.published_date = timezone.now()
                  employee.save()
                  return redirect('employee_detail', pk = employee.pk)
      else:
            form = EmployeeForm()
            return render(request,'salary/new_employee.html',{'form':form})
def edit_employee(request, pk):
      employee = get_object_or_404(Employee, pk=pk)
      if request.method == "POST":
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                  employee = form.save(commit=False)
                  employee.username = request.user
                  employee.name
                  employee.sector
                  employee.grade
                  employee.hrs
                  employee.rate
                  employee.salary
                  employee.published_date = timezone.now()
                  employee.save()
                  return redirect('employee_detail', pk = employee.pk)
      else:
            form = EmployeeForm(instance=employee)
            return render(request,'salary/edit_employee.html',{'form':form})
