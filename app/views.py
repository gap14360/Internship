from django.shortcuts import render
from .models import *

# Create your views here.

def InsertPageView(request):
    return render(request,"app/insert.html")


def InsertView(request):
    
    # Data come from HTML Page to Server!!
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']

    # Creating Object of Model Class!!
    # Inserting Data into Table!!

    newuser = Details.objects.create(Firstname=fname,Lastname=lname,Emails=email,Contacts=contact)

    # After Insert data render on Show page!!
    return render(request,"app/show.html")