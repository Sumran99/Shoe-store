from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages


def index(request):
   return render(request, "index.html")


def about(request):
    return render(request, "About.html")
    # return HttpResponse("This is about page")


def kids(request):
    return render(request, "kids.html")
    # return HttpResponse("This is about page")


def featured(request):
    return render(request, "Featured.html")
    # return HttpResponse("This is about page")

def contact(request):
    if request.method=="POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            query = request.POST.get("query")
            contact = Contact(name=name, email=email, phone=phone, desc=query, date=datetime.today())
            contact.save()
            messages.success(request, 'Your message has benn submitted!')

    return render(request, "contact.html")
    # return HttpResponse("This is about page")
