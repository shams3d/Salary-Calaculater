# Generated by Django 2.1.7 on 2019-03-01 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0011_employee_your_salary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='your_salary',
            field=models.IntegerField(default='0', editable=False),
        ),
    ]
