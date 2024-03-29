from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',include('DashBoard.urls')),
    path('careers/',include('jobUpdates.urls')),
    path('interview-experience/',include('InterviewExperienceApp.urls')),
    path('account/', include('users_app.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
