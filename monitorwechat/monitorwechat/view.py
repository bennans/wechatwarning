from django.http import HttpResponse
from mywxpy.sendmess import wechatsend
from django.shortcuts import render

def sendmess(request):
    mess = request.POST.get("mess","temp")
    wechatsend(mess)
    print(mess)
    return HttpResponse("YES")

def login(request):
    return render(request,"login.html")