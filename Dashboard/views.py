from django.shortcuts import render,redirect
from django.http import request
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == "POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            return render(request,'dashboard/login.html',{'error':'Username/ password is wrong'})
    else:
        return render(request,'dashboard/login.html')

    return render(request,'dashboard/login.html')


'''
we have used auth.login-----so this logout view is not necessary
def logout(request):
    if request.method == "POST":
        print("logout")
        auth.logout(request)
        return render(request,'dashboard/login.html')
'''
    

def dashboard(request):
    return render(request,'dashboard/dashboard.html')