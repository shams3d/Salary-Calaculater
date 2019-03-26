from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django_tables2 import RequestConfig
from .models import Employee
from .forms import EmployeeForm
from .tables import EmployeeTable
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from djchoices import DjangoChoices, ChoiceItem
from django.db.models import IntegerField, CharField, F, ExpressionWrapper, Count

def employee_list(request):
      #QuerySets
      employees= Employee.objects.filter(published_date__lte=timezone.now()).order_by('created_date')
      #Tables
      table = EmployeeTable(Employee.objects.filter(published_date__lte=timezone.now()).order_by('created_date'))
      RequestConfig(request,paginate={'per_page': 5}).configure(table)
      return render(request,'salary/employee_list.html',{'table':table})
def employee_details(request,pk):
      employee = get_object_or_404(Employee, pk=pk)
      return render(request, 'salary/employee_detail.html', {'employee': employee})
@login_required
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
                  employee.overtime
                  employee.salary 
                  employee.published_date = timezone.now()
                  employee.save()
                  return redirect('employee_detail', pk = employee.pk)
      else:
            form = EmployeeForm()
            return render(request,'salary/new_employee.html',{'form':form})
@login_required
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
                  employee.overtime
                  employee.salary
                  employee.published_date = timezone.now()
                  employee.save()
                  return redirect('employee_detail', pk = employee.pk)
      else:
            form = EmployeeForm(instance=employee)
            return render(request,'salary/edit_employee.html',{'form':form})
@login_required
def delete_employee(request, pk):
      employee= get_object_or_404(Employee, pk=pk)
      employee.delete()
      return redirect('employee_list')
def login_user(request, template_name='registration/login.html', extra_context=None):
      if request.POST.has_key('remember_me'):
            request.session.set_expiry(1209600) # 2 weeks
