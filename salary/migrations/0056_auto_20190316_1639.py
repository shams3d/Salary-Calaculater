# Generated by Django 2.1.7 on 2019-03-16 14:39

from django.db import migrations, models
import salary.models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0055_auto_20190316_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='overtime',
            field=models.FloatField(default='0'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(default='0', validators=[salary.models.Employee.hrs]),
        ),
    ]
