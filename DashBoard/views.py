from django.shortcuts import render

def Dashboard(request):
    return render(request, 'Dashboard/index.html', {})

def codehack_view(request):
    return render(request, 'Dashboard/codehack.html', {})

def Preparation(request):
    return render(request, 'Dashboard/interview_preparation.html', {})
