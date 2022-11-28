# Generated by Django 4.1.2 on 2022-11-28 12:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0020_remove_session_baserate_remove_session_costwithac"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentaccount",
            name="CGPA",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=4,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(10),
                ],
            ),
        ),
    ]