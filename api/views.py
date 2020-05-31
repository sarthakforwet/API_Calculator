from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from api.models import FacultyProfile
from django.views.generic.list import ListView
from api.models import Category, CategoryStream, Api, FacultyApi
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from api.forms import FacultyResgistrationForm, FacultyProfileForm, FacultyApiForm
from django.views.generic.base import TemplateView
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
import pandas as pd
from io import StringIO
import io
import csv
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

# class ActivityView(ListView):
#     context_object_name = 'activity_list'
#     def get_queryset(self,**kwargs):
#         current_user = User.objects.get(id=self.request.user.id)
#         current_user_stream = FacultyProfile.objects.get(user=current_user.id)
#         current_user_api_score = FacultyApi.objects.get(user=current_user.id)
#         if(self.kwargs['category_id'] == '7' or self.kwargs['category_id'] =='6'):
#             query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'])
#         else:
#             query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'], \
#                                                       stream=current_user_stream.stream)
#         return query

class ActivityView(TemplateView):
    template_name = "api/api_list.html"
    def get_context_data(self, **kwargs):
        current_user = User.objects.get(id=self.request.user.id)
        current_user_stream = FacultyProfile.objects.get(user=current_user.id)
        if(self.kwargs['category_id'] == '7' or self.kwargs['category_id'] =='6' \
                        or self.kwargs['category_id'] =='8'):

            query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'])
        else:
            query = Api.objects.filter(stream__category_id__id=self.kwargs['category_id'],\
                                        stream=current_user_stream.stream)
        context = {
            'activity_list' : query,
            # 'score_list': current_user_api_score,
            }
        return context

class FacultyApiView(FormView):
    template_name = "api/assesment_score.html"
    form_class = FacultyApiForm
    success_url = '/'
    def form_valid(self, form,**kwargs):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        try:
            x = form.save(commit=False)
            x.user = FacultyProfile.objects.get(user=User.objects.get(id=self.request.user.id))
            x.nature_of_activity = Api.objects.get(id=self.kwargs['nature_category_id'])
            x.save()
            return super().form_valid(form)
        except IntegrityError as e:
            return render(self.request, 'api/api_list.html', \
                {"message": "ERROR: Already added this field. Go to Update Section to update."})

class FacultyApiList(ListView):
    # model = FacultyApi
    context_object_name="list"
    def get_queryset(self,**kwargs):
        query = FacultyApi.objects.filter(user=FacultyProfile.objects.get(user=User.objects.get(id=self.request.user.id)))
        # query = FacultyApi.objects.all()
        return query

class FacultyApiUpdate(UpdateView):
    model = FacultyApi
    fields = ['self_assesment']
    success_url = reverse_lazy('api:list_view')



# Utility Function Corresponding to Generate API Report Link on nav-bar.
"""
Pending Work : Include the self-assessment Scores that faculty has filled till date.
"""
"""
Future Work : Include choice between xlsx or csv.
"""
def ApiReport(request):
    df = pd.DataFrame(columns=["Activity","Self_Assesment"]);
    query1 = Api.objects.values_list("nature_of_activity")
    query1 = [e for e in query1]
    query2 = FacultyApi.objects.values_list("self_assesment")
    query2 = [e for e in query2]
    df["Activity"] = query1
    df["Self_Assesment"] = 0
    print(df.head())
    sio = StringIO()
    cw = csv.writer(sio)
    cw.writerow(df.columns)
    for i in range(len(df)):
        cw.writerow(df.iloc[i])
    workbook = sio.getvalue()

    response = HttpResponse(workbook, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s' % "ar.csv"
    return response


