from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from psycopg2.extras import NumericRange
from django.utils import timezone

# Create your models here.
class Account(models.Model):
    accountID = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    #dob = models.DateTimeField(default=timezone.now())
    email = models.EmailField(max_length=100)
    passwd = models.CharField(max_length=50)
    personalContactNo = models.BigIntegerField(
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999)
        ]
    )
    gender = models.CharField(
        max_length=7,
        choices=[
            ('M', 'Male'),
            ('F', 'Female')
        ]
    )
    # accType = models.CharField(
    #     max_length = 10,
    #     choices=[
    #         ('Staff', 'Staff'),
    #         ('Student', 'Student')
    #     ]
    # )
    # dob = models.DateField(auto_now=False, auto_now_add=False)
    class Meta:
        abstract = True

class StudentAccount(Account):
    rollNo = models.BigIntegerField()
    branch = models.CharField(
        max_length=10,
        choices=[
            ('BE', 'BE'),
            ('BTECH', 'BTECH')
        ]
    )
    parentContactNo = models.BigIntegerField(
        validators=[
            MinValueValidator(1000000000),
            MaxValueValidator(9999999999)
        ]
    )
    currentRoomBooked = models.CharField(max_length=10, default='0')
    CGPA = models.DecimalField(max_digits=4, decimal_places=2)

class StaffAccount(Account):
    staffID = models.IntegerField()

class Session(models.Model):
    sessionID = models.AutoField(primary_key=True)
    startDate = models.DateField(auto_now=False, auto_now_add=False)
    endDate = models.DateField(auto_now=False, auto_now_add=False)
    minCGPA = models.DecimalField(max_digits=4, decimal_places=2)
    maxCGPA = models.DecimalField(max_digits=4, decimal_places=2)
    baseRate = models.DecimalField(max_digits=8, decimal_places=2)
    costWithAC= models.DecimalField(max_digits=8, decimal_places=2)

class Hostel(models.Model):
    name = models.CharField(max_length=50)
    numberOfRooms = models.PositiveIntegerField()

class Room(models.Model):
    roomNumber = models.PositiveIntegerField()
    hostelName = models.CharField(max_length=50)
    occupancy = models.PositiveIntegerField(default=0)
    availableSeats = models.PositiveIntegerField()
    roomType = models.CharField(
        max_length=10,
        choices=[
            ('AC', 'AC'),
            ('NONAC', 'NONAC')
        ]
    )
    blockTimeEnd = models.TimeField(default=timezone.now, auto_now=False)