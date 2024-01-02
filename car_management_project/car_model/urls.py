from django.urls import path,include
from . import views

urlpatterns = [
    # path('add_car/', views.add_car, name = 'add_car'),
    path('add_car/', views.AddCar.as_view(), name = 'add_car'),
]