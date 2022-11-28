# Generated by Django 4.1.2 on 2022-11-28 12:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0022_alter_staffaccount_email_alter_staffaccount_staffid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="cardNumber",
            field=models.BigIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1000000000000000),
                    django.core.validators.MaxValueValidator(9999999999999999),
                ]
            ),
        ),
    ]