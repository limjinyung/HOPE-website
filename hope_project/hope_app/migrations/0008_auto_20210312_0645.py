# Generated by Django 3.1.6 on 2021-03-12 06:45

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hope_app', '0007_auto_20210312_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='posttag',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='posttag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 12, 6, 45, 15, 132444, tzinfo=utc)),
        ),
    ]
