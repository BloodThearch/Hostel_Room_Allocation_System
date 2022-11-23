from django.shortcuts import render
from db.models import Session

# Create your views here.
def showDashboard(request, dictRecord={}):
    dictRecord = createCGPAList(dictRecord)
    return render(request, 'dashboard.html', dictRecord)

def createCGPAList(dictRecord):
    dictRecord['booking'] = 'closed'
    try:
        sessions = Session.objects.all().values()
        for session in sessions:
            if dictRecord['CGPA'] >= session['minCGPA'] and dictRecord['CGPA'] <= session['maxCGPA']:
                dictRecord['booking'] = 'open'
    except:
        pass
    return dictRecord