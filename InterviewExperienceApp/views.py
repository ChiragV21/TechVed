from django.shortcuts import render, get_object_or_404
from .models import InterviewExperience

def all_posts(request):
    posts = InterviewExperience.objects.all()
    print(posts)
    return render(request, 'InterviewExperienceApp/all_experience.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(InterviewExperience, slug=slug)
    return render(request, 'InterviewExperienceApp/experience_detail.html', {'post': post})