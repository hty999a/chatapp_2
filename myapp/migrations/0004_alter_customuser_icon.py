# Generated by Django 5.0.2 on 2024-02-28 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customuser_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='icon',
            field=models.FileField(default='/', upload_to=''),
        ),
    ]
