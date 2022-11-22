from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from db.models import *

# Create your views here.
def showLoginPage(request):
    return render(request, 'login.html', {
        "email":"",
        "passwd":"",
        "err":""
    })

@csrf_exempt
def loginCheck(request):
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["pwd"]
        err = "Please provide valid email or password."
        sendback = {
                "email": email,
                "passwd": pwd,
                "err": err
            }
        try:
            fetchedRecord = StudentAccount.objects.get(email=email)
            if pwd == fetchedRecord.passwd:
                return render(request, 'home.html', {"StudentInfo":fetchedRecord})
            else:
                return render(request, "login.html", sendback)
        except:
            pass
        try:
            fetchedRecord = StaffAccount.objects.get(email=email)
            if pwd == fetchedRecord.passwd:
                return render(request, 'home.html', {"StaffInfo":fetchedRecord})
            else:
                return render(request,'login.html',sendback)
        except:
            pass
        return render(request, 'login.html', sendback)

