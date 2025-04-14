from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api_1_3.urls')),
    path('api_admin/', include('api_admin.urls')),
    path('auth/', include('api_auth.urls')),


]
