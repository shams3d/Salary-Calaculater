# Generated by Django 2.1.7 on 2019-03-03 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0022_auto_20190303_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hrs',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.FloatField(max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(default='0'),
        ),
    ]
