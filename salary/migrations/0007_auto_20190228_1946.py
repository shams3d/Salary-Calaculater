# Generated by Django 2.1.7 on 2019-02-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0006_auto_20190228_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(blank=True, default='Enter your Name here...', max_length=50),
        ),
    ]