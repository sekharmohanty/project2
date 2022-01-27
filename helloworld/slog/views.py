from django.shortcuts import redirect, render
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        username=request.POST['user']
        password=request.POST['pass']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('login')
    else:

        return render (request,"login.html")