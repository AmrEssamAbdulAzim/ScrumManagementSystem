# Generated by Django 2.0.1 on 2018-01-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backlog', '0002_auto_20180127_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlog',
            name='start_at',
            field=models.DateField(auto_now=True),
        ),
    ]
