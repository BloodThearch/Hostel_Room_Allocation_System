# Generated by Django 4.1.2 on 2022-11-28 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0019_transaction"),
    ]

    operations = [
        migrations.RemoveField(model_name="session", name="baseRate",),
        migrations.RemoveField(model_name="session", name="costWithAC",),
    ]