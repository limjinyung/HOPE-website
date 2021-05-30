# Generated by Django 3.1.6 on 2021-03-12 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hope_app', '0006_volunteerexperience_portfolio'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hope_app.posttag'),
        ),
    ]
