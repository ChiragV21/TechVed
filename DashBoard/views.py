from django.shortcuts import render
from CodHackApp.models import CodHack
# Create your views here.
def Dashboard(request):
    return render(request,'Dashboard/index.html',{})

def CodeHack(request):
    all_challenges=CodHack.objects.all()
    return render(request,'Dashboard/codehack.html',{'all_challenges':all_challenges})