from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
]