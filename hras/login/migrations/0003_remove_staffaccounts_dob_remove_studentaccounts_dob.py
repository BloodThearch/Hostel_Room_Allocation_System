# Generated by Django 4.1.2 on 2022-11-18 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("login", "0002_remove_staffaccounts_age_remove_studentaccounts_age_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="staffaccounts", name="dob",),
        migrations.RemoveField(model_name="studentaccounts", name="dob",),
    ]