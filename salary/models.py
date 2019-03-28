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
    def hrs(value):
        value = round(20,2)

    def rate(value):
        value = round(0,2)
    def rate(value):
        value = round(0,2)



    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null=False,blank = False)
    sector = models.CharField(max_length=100, choices = SectorChoice.choices, default = 'HR')
    grade = models.CharField(max_length = 20, choices = GradeChoice.choices, default = 'A', null=True)
    hrs = models.FloatField(blank = False, validators = [hrs])
    rate = models.FloatField(blank = False, validators = [rate])
    overtime= models.FloatField(default="0", blank=True, null=True)
    salary = models.FloatField(default="0", blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def save(self, *args, **kwargs):
        if self.hrs <= 20:
            self.overtime = 0
        elif self.hrs >= 20:
            self.overtime = round(self.hrs - 20,2) + round(self.rate * 1.5,2)
            pass
        try:
            self.salary= self.overtime + self.hrs * self.rate
        except TypeError:
            pass
        super(Employee,self).save(*args, **kwargs)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __int__(self):
        return self.save()

    def __str__(self):
        return '' + self.name
