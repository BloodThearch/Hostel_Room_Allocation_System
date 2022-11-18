from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Accounts(models.Model):
    accountID = models.IntegerField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=7,
        choices=[
            ('Genders', 'Male Female')
        ]
    )
    # dob = models.DateField(auto_now=False, auto_now_add=False)
    class Meta:
        abstract = True

class StudentAccounts(Accounts):
    rollNo = models.IntegerField()
    branch = models.CharField(
        max_length=10,
        choices=[
            ('Branches', 'BE BTECH')
        ]
    )
    parentContactNo = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])
    currentRoomBooked = models.CharField(max_length=10)
    CGPA = models.DecimalField(max_digits=2, decimal_places=2)

class StaffAccounts(Accounts):
    staffID = models.IntegerField()