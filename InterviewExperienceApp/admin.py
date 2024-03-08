from django.contrib import admin
from .models import InterviewExperience

class InterviewExperienceAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contributor_name', 'contributor_email', 'created_by', 'created_date')
    search_fields = ('company_name', 'contributor_name', 'contributor_email')
    list_filter = ('created_date',)

admin.site.register(InterviewExperience,InterviewExperienceAdmin)