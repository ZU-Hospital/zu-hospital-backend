# Generated by Django 5.0.3 on 2024-05-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("visit", "0002_remove_visit_datatime_visit_end_at_visit_start_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="attachment",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="attachment",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AddField(
            model_name="visit",
            name="deleted",
            field=models.DateTimeField(db_index=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name="visit",
            name="deleted_by_cascade",
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
