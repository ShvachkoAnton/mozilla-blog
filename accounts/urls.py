from . import views
from django.urls import path,include
urlpatterns = [
    path('login', views.user_login, name='login'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
