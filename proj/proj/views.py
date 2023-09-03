from django.shortcuts import render
from django.http import HttpResponse
from . form import student

def home(request):
    data={}
    d=student()
    try: 
        n1=request.POST.get("fname")
        n2=request.POST.get("lname")
        data={
            'a':n1,
            'b':n2,
            'f':d
        }
    except:
        pass

    return render(request,"index.html",data)