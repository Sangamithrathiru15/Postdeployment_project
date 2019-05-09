from django.shortcuts import render
from django.http import request,HttpResponse
from  .models import FileData


def pilot(request):
    return render(request,'pilot/pilotchecks.html')

    

def displaydata(request):
    if request.method=="POST":
        data=FileData.objects.all()
        store_status={}
        for d in data:
            if (d.progressrjbridge_GB=='1.0.87' and d.commonutilities_GB=='1.0.87' and d.callcentreinstore_GB=='1.0.87' and d.rjsoabridge_GB=='1.0.87' and d.socrates_GB=='1.0.87'
            and d.retailjstaticdata_UK=='1.13.25' and d.storeserver_GB=='1.5.83' and d.storeprogresscode_GB=='1.4.18'):
                store_status[d.store_number]="Upgraded"
                print(store_status[d.store_number])
            else:
                store_status[d.store_number]="Not upgraded"
        return(render(request,'pilot/displaypilot.html',{"info":FileData.objects.all()},store_status))

