# Generated by Django 2.1.7 on 2019-03-03 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0018_auto_20190303_1754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
    ]
