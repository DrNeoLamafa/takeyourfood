
from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    
    path('', views.index, name="index"),
    path('foodlist/<slug>/', views.foodlist, name="foodlist_url")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
