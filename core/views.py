from django.shortcuts import render

# Create your views here.

"""
def login_user(request):
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('/')
"""

def home(request):
    return render(request, 'home.html')