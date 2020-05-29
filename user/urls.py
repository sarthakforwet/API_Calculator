from django.urls import path
from user import views
from user.views import FacultyRegistration
from django.contrib.auth.views import LoginView,LogoutView
from user.forms import MyAuthForm
app_name = 'user'

urlpatterns = [
    path('register/', views.FacultyRegistration.as_view(),name="register" ),
    path('login/', LoginView.as_view(template_name='user/login.html',authentication_form=MyAuthForm),name='login'),

]
