# Generated by Django 2.1.7 on 2019-03-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0019_remove_employee_salary'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.FloatField(default='0', max_length=50),
        ),
    ]
