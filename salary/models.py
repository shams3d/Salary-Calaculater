# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from djchoices import DjangoChoices, ChoiceItem
from django.db.models import FloatField, CharField, F, ExpressionWrapper, IntegerField


class Employee(models.Model):
    
    class SectorChoice(DjangoChoices):
            HR = ChoiceItem("HR")
            Audit = ChoiceItem("Audit")
            Customers = ChoiceItem("Customers")
            Sales = ChoiceItem("Sales")
    class GradeChoice(DjangoChoices):
            A = ChoiceItem("A")
            B = ChoiceItem("B")
            C = ChoiceItem("C")
            D = ChoiceItem("D")
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,default = "Enter Employee Name here...", blank = False)
    sector = models.CharField(max_length=100, choices = SectorChoice.choices, default = 'HR')
    grade = models.CharField(max_length = 20, choices = GradeChoice.choices, default = 'A', null=True)
    hrs = models.PositiveIntegerField(default ="0")
    rate = models.PositiveIntegerField(default="0")
    salary = models.PositiveIntegerField(null=True, blank=True, default="0",editable=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Employees'
        verbose_name_plural = 'Employee'
    
    
    
    def save(self, *args, **kwargs):
        try:
            self.salary=self.hrs * self.rate
        except TypeError:
            pass
        super(Employee,self).save(*args, **kwargs)
        
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        

    def __int__(self):
        return self.salary()
    
    def __str__(self):
        return '' + self.name 
   
