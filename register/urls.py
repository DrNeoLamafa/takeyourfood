
from .views import register, LkRender
from django.urls import path
from django.contrib.auth import views



urlpatterns = [
    
    path('register/', register, name='register'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('lk/', LkRender, name="LkRender")

]