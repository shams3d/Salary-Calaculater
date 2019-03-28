# Generated by Django 2.1.7 on 2019-03-26 17:53

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0063_auto_20190317_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(validators=[salary.models.Employee.hrs]),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.FloatField(validators=[salary.models.Employee.rate]),
        ),
    ]