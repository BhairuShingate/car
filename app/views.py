from django.shortcuts import render

# Create your views here.
import json
file = open(r'D:\Jango\car\app\car.json','r')
json_data = file.read()
py_data = json.loads(json_data)

cars = py_data["cars"]

def rental(request):
    context = {
        'cars' : cars
    }
    return render(request,'carrental.html',context)
file.close()


def one_car(request,num):
    context={
        'car' : cars[num-1]
    }
    return render(request,'carlist.html',context)

def about_page(request):
    return render(request,'about.html')

def cont_page(request):
    return render(request,'contact.html')

def login_page(request):
    return render(request,'login.html')

def register_page(request):
    return render(request,'register.html')