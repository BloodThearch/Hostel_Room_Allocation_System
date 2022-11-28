from django.shortcuts import render
from db.models import Session, StudentAccount

# Create your views here.
def showDashboard(request, dictRecord={}):
    dictRecord = createCGPAList(request.session['email'], dictRecord)
    print('email =', request.session['email'])
    return render(request, 'dashboard.html', dictRecord)

def createCGPAList(email, dictRecord):
    dictRecord['booking'] = 'closed'
    try:
        sessions = Session.objects.all().values()
        for session in sessions:
            if dictRecord['CGPA'] >= session['minCGPA'] and dictRecord['CGPA'] <= session['maxCGPA']:
                dictRecord['booking'] = 'open'
                break
    except:
        pass
    try:
        if StudentAccount.objects.get(email=email).currentRoomBooked != '0':
            dictRecord['booking'] = 'closed'
    except:
        pass
    return dictRecord

def hostelDesc(request):
    return render(request, 'hostelDesc.html', {})