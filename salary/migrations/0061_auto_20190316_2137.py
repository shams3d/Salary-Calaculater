# Generated by Django 2.1.7 on 2019-03-16 19:37

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0060_auto_20190316_2135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(default='0', validators=[salary.models.Employee.hrs]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
