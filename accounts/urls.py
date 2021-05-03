from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView


app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name="register"),
]
