from django.shortcuts import redirect, render
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username=request.POST['user']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass']
        user=User.objects.create_user(username=username,first_name=fname,last_name=lname,email=email,password=password)
        user.save()
        print('user created sucessfully')
        return redirect('/')
    else:

        return render(request,"form.html")