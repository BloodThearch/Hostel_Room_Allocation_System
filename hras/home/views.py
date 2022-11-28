from django.shortcuts import render

# Create your views here.
def showHomePage(request):
    isMessage = True
    request.session['email'] = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            email = request.POST["email"]
            subject = request.POST["subject"]
            message = request.POST["message"]
            print("###---------------------")
            print("Name:", name)
            print("Email:", email)
            print("Subject", subject)
            print("Message:", message)
            print("###---------------------")
    except:
        isMessage = False
    return render(request, 'home.html', {})
