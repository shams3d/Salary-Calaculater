# Generated by Django 2.1.7 on 2019-03-06 10:50

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('salary', '0030_auto_20190306_1338'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SalarySys',
            new_name='Employee',
        ),
        migrations.DeleteModel(
            name='EmployeeForm',
        ),
        migrations.DeleteModel(
            name='EmployeeInfo',
        ),
        migrations.DeleteModel(
            name='EmployeeSalary',
        ),
    ]