from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def welcome(request):
    return render(request, "Website/welcome.html", {"meetings": Meeting.objects.all()})


def date(request):
    return HttpResponse("This page will be served at " + str(datetime.now()))


def about(request):
    return HttpResponse("This is a website created by Zachary Kaiser for APC 440")
