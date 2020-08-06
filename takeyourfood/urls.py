
from django.contrib import admin
import register
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainblock.urls')),
    path('', include('register.urls')),
    path('', include('lk.urls')),
    

]
