from django.shortcuts import render
from django.template.defaulttags import csrf_token
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.forms.models import model_to_dict
from db.models import *
from dashboard.views import showDashboard

# Create your views here.
def showLoginPage(request):
    return render(request, 'login.html', {
        "email":"",
        "passwd":"",
        "err":""
    })

@csrf_exempt
def loginCheck(request):
    dictRecord = {}
    if request.method == "POST":
        email = request.POST["email"]
        pwd = request.POST["pwd"]
        err = "Please provide valid email or password."
        sendback = {
                "email": email,
                "passwd": pwd,
                "err": err
            }
        studentSuccess = True
        try:
            fetchedRecord = StudentAccount.objects.get(email=email)
            if str(pwd) == str(fetchedRecord.passwd):
                print(1)
                dictRecord = model_to_dict(fetchedRecord)
                dictRecord["accType"] = "Student"
                #showDashboard(request, dictRecord)
                print(2)
            else:
                return render(request, "login.html", sendback)
        except:
            studentSuccess = False
        success = True
        try:
            fetchedRecord = StaffAccount.objects.get(email=email)
            if pwd == fetchedRecord.passwd:
                dictRecord = model_to_dict(fetchedRecord)
                dictRecord["accType"] = "Staff"
                #showDashboard(request, dictRecord)
            else:
                return render(request,'login.html',sendback)
        except:
            success = False
        if studentSuccess == True:
            request.session['email'] = dictRecord['email']
            if dictRecord["accType"] == "Student":
                return showDashboard(request, dictRecord)
            elif dictRecord["accType"] == "Staff":
                return showDashboard(request, dictRecord)
        if success == True:
            request.session['email'] = dictRecord['email']
            if dictRecord["accType"] == "Student":
                return showDashboard(request, dictRecord)
            elif dictRecord["accType"] == "Staff":
                return showDashboard(request, dictRecord)
        return render(request, 'login.html', {"err":"Please provide valid email or password."})

