from django.contrib import admin
from .models import InterviewExperience

class InterviewExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'role', 'experience', 'contributor_name', 'contributor_email', 'created_date')

admin.site.register(InterviewExperience,InterviewExperienceAdmin)