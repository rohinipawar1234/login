from django.shortcuts import render,redirect
from .models import*
# Create your views here

def Index(request):
    return render(request,'register.html')

def Showdata(request):
    a = Student.objects.all()
    return render(request,"show.html",{'user':a}) 

def Loginpage(request):
    return render(request,"loginpage.html")


def Updatepage(request):
    return render (request,"update.html")    




def Deletedata(request,id):
    b = Student.objects.get(id=id)
    b.delete()
    return redirect("showdata")    

def Register(request):
    if request.method=="POST":

     
        First_name = request.POST['first_name']
        Last_name = request.POST['last_name']
        Address = request.POST['address']
        Email = request.POST['email']


        std = Student.objects.create(first_name = First_name,
                                     last_name = Last_name,
                                     address = Address,
                                     email = Email,
                            )

    return redirect("showdata")