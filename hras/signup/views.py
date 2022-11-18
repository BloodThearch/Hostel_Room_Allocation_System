from django.shortcuts import render

# Create your views here.
def showSignupPage(request):
    return render(request, 'signup.html', {})