from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('login', views.log_in, name="login"),
    path('signout', views.log_out, name="signout"),
    path('signup', views.signup, name="signup"),
    path('<str:room_name>/', views.room, name='room'),
]