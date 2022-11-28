# Generated by Django 4.1.2 on 2022-11-28 12:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("db", "0023_alter_transaction_cardnumber"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="expiryMonth",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(12),
                ]
            ),
        ),
    ]
