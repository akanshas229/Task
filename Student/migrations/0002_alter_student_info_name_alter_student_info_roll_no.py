# Generated by Django 4.1.dev20211224103900 on 2022-01-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_info',
            name='Name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='student_info',
            name='Roll_no',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
