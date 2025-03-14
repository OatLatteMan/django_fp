from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('django_fp/', include('django_fp.urls', namespace='django_fp')),

    path('admin/', admin.site.urls),
]
