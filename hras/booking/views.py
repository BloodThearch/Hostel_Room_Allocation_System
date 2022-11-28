from django.shortcuts import render
from db.models import Hostel, StudentAccount, Room, Transaction
from django.forms.models import model_to_dict
from django.utils import timezone
import datetime

# Create your views here.
def hostelList(request):
    print('hostel list session email = ', request.session['email'])
    studentRecord = StudentAccount.objects.get(email=request.session['email'])
    hostels = Hostel.objects.filter(forGender=studentRecord.gender).values()
    return render(request, 'hostelList.html', {"hostels":hostels})

def roomList(request):
    if request.method == "POST":
        hostelName = request.POST["hostelName"]
        request.session['hostelName'] = hostelName
        rooms = Room.objects.filter(hostelName=hostelName).values()
        roomNoList = []
        for room in rooms:
            if room["isBlocked"] == 1 and room["blockTimeEnd"] > timezone.now().time():
                pass
            else:
                roomNoList.append([room["roomNumber"],room["roomType"]])
        return render(request, 'roomList.html', {"roomNoList":roomNoList})

def paymentPortal(request):
    if request.method == "POST":
        try:
            roomNumber = request.POST["roomID"]
            request.session['roomNumber'] = roomNumber
        except:
            roomNumber = request.session['roomNumber']
        hostelName = request.session['hostelName']
        roomType = Room.objects.filter(hostelName=hostelName).get(roomNumber=roomNumber).roomType

        Room.objects.filter(hostelName=hostelName).filter(roomNumber=roomNumber).update(isBlocked=1, blockTimeEnd=timezone.now() + datetime.timedelta(minutes=15))

        if roomType == "NONAC":
            amount = 70000
        elif roomType == "AC":
            amount = 85000
        request.session['amount'] = amount
        return render(request, 'paymentPage.html', {
            'roomNumber':roomNumber,
            'hostelName':hostelName,
            'amount':amount
        })

def paymentCheck(request):
    if request.method == "POST":
        cardNumber = request.POST["cardNo"]
        expiryMonth = request.POST["expiryMonth"]
        expiryYear = request.POST["expiryYear"]
        cardHolderName = request.POST["name"]
        securityCode = request.POST["securityCode"]
        hostelName = request.session["hostelName"]
        roomNumber = request.session["roomNumber"]
        amount = request.session["amount"]

        sendback = {
            "cardNumber":cardNumber,
            "expiryMonth":expiryMonth,
            "expiryYear":expiryYear,
            "cardHolderName":cardHolderName,
            "securityCode":securityCode,
            "hostelName":hostelName,
            "roomNumber":roomNumber,
            "amount":amount,
            'err':'Invalid Details.'
        }

        success = True
        try:
            transaction = Transaction(
                cardNumber=cardNumber,
                expiryMonth=expiryMonth,
                expiryYear=expiryYear,
                cardHolderName=cardHolderName,
                securityCode=securityCode,
                hostelName=hostelName,
                roomNumber=roomNumber,
                amount=amount
            )
            transaction.save()
        except:
            success=False
        if success==False:
            return render(request, 'paymentPage.html', sendback)
        else:
            student = StudentAccount.objects.get(email=request.session['email'])
            student.currentRoomBooked = hostelName + " " + str(roomNumber)
            student.save()
            occupancy = Room.objects.filter(hostelName=hostelName).get(roomNumber=roomNumber).occupancy
            Room.objects.filter(hostelName=hostelName).filter(roomNumber=roomNumber).update(isBlocked=0, occupancy=occupancy+1)
            return render(request, 'dashboard.html', {'accType':'Student','booking':'closed'})