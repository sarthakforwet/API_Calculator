from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from api.models import FacultyProfile
from django.views.generic.list import ListView
from api.models import Category, CategoryStream, Api
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from api.forms import FacultyResgistrationForm, FacultyProfileForm, FacultyApiForm
from django.views.generic.base import TemplateView

class FacultyRegistration(FormView):
    template_name = "user/faculty_registration.html"
    form_class = FacultyResgistrationForm
    success_url = 'complete_profile/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)

class FacutyProfileView(FormView):
    template_name = "user/faculty_registration.html"
    form_class = FacultyProfileForm
    success_url = '/done/'
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        a = form.save(commit=False)
        a.user = User.objects.get(id=self.request.user.id)
        a.save()
        return super().form_valid(form)

class BaseView(TemplateView):
    template_name = "base.html"


class CategoryView(ListView):
    context_object_name = 'category_list'
    def get_queryset(self,**kwargs):
        query = Category.objects.all()
        return query

class ActivityView(ListView):
    context_object_name = 'activity_list'
    def get_queryset(self,**kwargs):
        current_user = User.objects.get(id=self.request.user.id)
        current_user_stream = FacultyProfile.objects.get(user=current_user.id)
        if(self.kwargs['category_id'] == '7' or self.kwargs['category_id'] =='6'):
            query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'])
        else:
            query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'],stream=current_user_stream.stream)
        return query

class FacultyApiView(FormView):
    template_name = "api/assesment_score.html"
    form_class = FacultyApiForm
    success_url = '/done/'
    def form_valid(self, form,**kwargs):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        x = form.save(commit=False)
        x.user = FacultyProfile.objects.get(user=User.objects.get(id=self.request.user.id))
        x.nature_of_activity = Api.objects.get(id=self.kwargs['nature_category_id'])
        x.save()
        return super().form_valid(form)