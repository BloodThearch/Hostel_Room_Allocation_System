# Generated by Django 4.1.2 on 2022-11-22 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0003_hostel_room_sessions"),
    ]

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                ("sessionID", models.AutoField(primary_key=True, serialize=False)),
                ("startDate", models.DateField()),
                ("endDate", models.DateField()),
                ("minCGPA", models.DecimalField(decimal_places=2, max_digits=4)),
                ("maxCGPA", models.DecimalField(decimal_places=2, max_digits=4)),
                ("baseRate", models.DecimalField(decimal_places=2, max_digits=8)),
                ("costWithAC", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.DeleteModel(name="Sessions",),
    ]
