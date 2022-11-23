from django.shortcuts import render
from db.forms import SessionForm

# Create your views here.
def showSessionCreation(request):
    return render(request, 'makeSession.html', {"form":SessionForm()})

def sessionCheck(request):
    if request.method == "POST":
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard.html', {"accType":"Staff"})
        else:
            return render(request, 'makeSession.html', {"err":"Enter valid details."})