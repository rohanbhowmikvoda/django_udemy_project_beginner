from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',views.register_user,name='register_user'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'), #LoginView is a class based View and hence as_view() is used
    path('logout/',views.logout_view,name='logout'),
]