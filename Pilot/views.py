from django.shortcuts import render
from django.http import request,HttpResponse
import csv
import re
def pilot(request):
    return render(request,'pilot/pilotchecks.html')

    

def extractdata(request):
    if request.method == "POST":
        uploaded_file=request.FILES['uploaded_files/checks.csv']
        file_reader = csv.reader(uploaded_file, delimiter=',')
        for row in file_reader:
        # do something with row data.
            print(row)
        return render(request,'pilot/output.html',{"data":file_reader})
'''
        data = uploaded_file.read()
        rows = re.split('\n', data)
        for index, row in enumerate(rows):
            cells = row.split(',')
        return render(request,'pilot/output.html',{"data":cells})



def handle_uploaded_file(f):
    with open('uploaded_files/checks.csv', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
        '''