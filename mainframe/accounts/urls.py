from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import custom_logout
from .views import index_recipe


urlpatterns = [
    path('', views.home , name='home'),
    path('mainframe/', views.mainframe, name='mainframe'),
    path('info/', views.info, name='info'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('custom_logout/', custom_logout, name='custom_logout'),
    path('success/', views.success_page, name='success_page'),
    path('recipe/', views.index_recipe, name='index_recipe'),
    path('sparkle/', views.sparkle, name='sparkle'),
     path('main/', views.main, name='main'),



]
