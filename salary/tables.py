import django_tables2 as tables
from django_tables2 import A
from .models import Employee




class EmployeeTable(tables.Table):
    id = tables.Column(attrs={'td': {'class': 'table-danger'}})
    name = tables.LinkColumn("employee_detail", kwargs={"pk": tables.A("pk")}, empty_values=())
    sector = tables.Column()
    salary = tables.Column(footer=lambda total,salary: sum(total['salary']))
  
    
    class Meta:
        model = Employee
        fields = ('id', 'name', 'sector', 'salary')
        attrs = {'class': 'table'}
        template_name = 'django_tables2/bootstrap4.html'
        

