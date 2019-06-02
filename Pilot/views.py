from django.shortcuts import render,get_object_or_404
from django.http import request,HttpResponse
from  .models import FileData
from django.contrib.auth.decorators import login_required

@login_required(login_url="/home/")
def pilot(request):
    return render(request,'pilot/pilotchecks.html')

    

def displaydata(request,store_num):
    if request.method=="POST":
        print(store_num)
        data=get_object_or_404(FileData,store_number=store_num)
        print(data)
        return(render(request,'pilot/displaypilot.html',{"storedata":data}))

