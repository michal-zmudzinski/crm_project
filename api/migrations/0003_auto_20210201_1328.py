# Generated by Django 3.1.4 on 2021-02-01 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210201_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(max_length=16, unique=True),
        ),
    ]
