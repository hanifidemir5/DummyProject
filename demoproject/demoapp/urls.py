from django.urls import path
from . import views

urlpatterns = [
    path('home_demo', views.home_demo),
    path('menu/', views.menu),
    path('about/', views.about),
    path('demoform/', views.demo_form_view),
    path('anime/', views.animekizlari),
    path('date/', views.display_date),
    path('dishes/<str:dish>/', views.menuitems),
    path('menu_card/', views.menu_by_id),
    path('', views.home, name='home'), 
    path('register/', views.register, name='register'),  
    path('login/', views.login, name='login'), 
]