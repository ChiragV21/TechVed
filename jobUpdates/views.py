from django.shortcuts import render
from .models import CompanyDetails

def CareerPage(request):
    all_jobs=CompanyDetails.objects.all()
    return render(request, 'jobUpdates/all_jobs.html',{'all_jobs':all_jobs})