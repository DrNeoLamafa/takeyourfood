

from django.urls import path
from lk import views


urlpatterns = [
    
    path('lk/', views.lk, name='lk'),
    path('logout/', views.LogoutView.as_view(), name='logout')

]