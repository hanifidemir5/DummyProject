from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('demoform/', views.demo_form_view),
    path('anime/', views.animekizlari),
    path('date/', views.display_date),
    path('dishes/<str:dish>/', views.menuitems),
]