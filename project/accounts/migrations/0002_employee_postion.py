# Generated by Django 5.0.3 on 2024-05-19 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="employee",
            name="postion",
            field=models.CharField(default="test", max_length=255),
        ),
    ]
