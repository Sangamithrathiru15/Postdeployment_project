from django.shortcuts import render,get_object_or_404
from django.http import request
from  Pilot.models import FileData
from django.contrib.auth.decorators import login_required

def basiccheck(request):
    return render(request,'basiccheck/basicchecks.html')

@login_required(login_url="/home/")
def basicresult(request,store_num):
    if request.method=="POST":
        print(store_num)
        data=get_object_or_404(FileData,store_number=store_num)
        print(data)
        return(render(request,'basiccheck/displaybasic.html',{"storedata":data}))