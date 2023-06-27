from django.shortcuts import render

# Create your views here.


def login(request):
    return render(request, 'auth/auth-signin.html')

def dashboard(request):
    return render(request, 'dashboard/add-record.html')