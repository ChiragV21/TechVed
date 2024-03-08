from django.contrib import admin
from .models import CompanyDetails
# Register your models here.
class CompanyDetailsAdmin(admin.ModelAdmin):
    list_display=('created_by','created_date','name','role','location','url','batch')
    
admin.site.register(CompanyDetails,CompanyDetailsAdmin)