from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from user.forms import FacultyResgistrationForm, FacultyProfileForm

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
