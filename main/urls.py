from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('auth/', views.auth_page, name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('animals/', views.animals, name='animals'),
    path('about/', views.about, name='about'),
]