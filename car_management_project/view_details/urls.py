from django.urls import path,include
from . import views

urlpatterns = [
    path('details/<int:id>/', views.DetailPostView.as_view(), name = 'details'),
    path('purchase/<int:id>', views.purchase_history, name = 'purchase'),
]