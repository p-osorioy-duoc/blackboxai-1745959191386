from django.urls import path
from . import views

app_name = "vehicles"

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('vehicle/add/', views.vehicle_add, name='vehicle_add'),
    path('vehicle/<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
    path('vehicle/<int:pk>/maintenance/add/', views.maintenance_add, name='maintenance_add'),
    path('vehicle/<int:pk>/repair/add/', views.repair_add, name='repair_add'),
]
