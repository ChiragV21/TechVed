from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.Dashboard,name='Dashboard'),
    path('events/',views.CodeHack,name='CodeHack'),
]