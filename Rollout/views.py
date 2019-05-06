from django.shortcuts import render
from django.http import request

def rollout(request):
    return render(request,'rollout/rolloutchecks.html')
