# Generated by Django 5.0.2 on 2024-02-28 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='icon',
        ),
    ]
