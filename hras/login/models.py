from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Accounts(models.Model):
    accountID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    age = models.IntegerField()
    class Meta:
        abstract = True

class StudentAccounts(Accounts):
    rollNo = models.IntegerField()
    branch = models.Choices([
        ('BE', 'Bachelors in Engineering'),
        # Add more branches later
    ])
    parentContactNo = PhoneNumberField