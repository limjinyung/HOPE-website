# Generated by Django 3.1.6 on 2021-03-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hope_app', '0003_auto_20210309_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerexperience',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='volunteerexperience',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateField(),
        ),
    ]
