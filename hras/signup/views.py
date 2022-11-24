from django.shortcuts import render
from db.forms import StudentRegistrationForm, StaffRegistrationForm

# Create your views here.
def chooseSignup(request):
    return render(request, 'chooseSignup.html', {})

def studentSignup(request):
    return render(request, 'studentSignup.html', {'form':StudentRegistrationForm()})

def staffSignup(request):
    return render(request, 'staffSignup.html', {'form':StaffRegistrationForm()})

def studentSignupCheck(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {})
        else:
            return render(request, 'studentSignup.html', {'err':"Invalid Details."})

def staffSignupCheck(request):
    if request.method == "POST":
        form = StaffRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {})
        else:
            return render(request, 'staffSignup.html', {'err':"Invalid Details."})