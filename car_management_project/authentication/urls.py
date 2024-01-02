from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.UserLogIn.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.display_purchase_history, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('password_change/', views.password_change, name='password_change'),
]