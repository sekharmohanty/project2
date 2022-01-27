from django.shortcuts import render

# Create your views here.
def home(request):

    return render (request,"h.html",{"name":"raghav",'link':' http://127.0.0.1:8000/'})
def profile(request):
    return render(request,"h.html",{"name":"profiles",'link':' http://127.0.0.1:8000/'})
def mul(request):
    v1=int(request.POST['val1'])
    v2=int(request.POST['val2'])
    v3=v1*v2
    return render(request,'op.html',{'res':v3})