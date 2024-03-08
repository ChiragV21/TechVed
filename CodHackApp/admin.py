from django.contrib import admin
from .models import CodHack

class CodHackAdmin(admin.ModelAdmin):
    list_display=('created_by','created_date','name','images','url','start_date','end_date','event_type')
    
admin.site.register(CodHack,CodHackAdmin)
