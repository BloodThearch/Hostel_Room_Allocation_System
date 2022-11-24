from django.shortcuts import render

# Create your views here.
def hostelList(request):
    print('hostel list session email = ', request.session['email'])
    return render(request, 'hostelList.html', {})