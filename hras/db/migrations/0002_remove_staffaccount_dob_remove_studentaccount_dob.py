# Generated by Django 4.1.2 on 2022-11-22 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="staffaccount", name="dob",),
        migrations.RemoveField(model_name="studentaccount", name="dob",),
    ]
