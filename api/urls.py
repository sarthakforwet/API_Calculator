from django.urls import path
from api import views
from django.urls import path
# from us.views import FacultyRegistration, FacutyProfileView
from django.contrib.auth.views import LoginView,LogoutView
from api.forms import MyAuthForm

app_name = 'api'

urlpatterns = [
    path('',views.BaseView.as_view(),name="index"),
    path('register/', views.FacultyRegistration.as_view(),name="register" ),
    path('login/', LoginView.as_view(template_name='user/login.html',authentication_form=MyAuthForm),name='login'),
    path('register/complete_profile/', views.FacutyProfileView.as_view(),name="profile"),
    path('category',views.CategoryView.as_view(),name='category'),
    path('category/<category_id>/', views.ActivityView.as_view(),name="activity"),
    path('category/<category_id>/<nature_category_id>', views.FacultyApiView.as_view(),name="activity_form"),
]
