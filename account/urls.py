from django.urls import path
from .views import dashboard
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'
urlpatterns = [
    #path('login/', login, name='login'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('dashboard/', dashboard, name='dashboard')
    ]