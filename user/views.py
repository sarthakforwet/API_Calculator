from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.edit import FormView
from user.forms import FacultyResgistrationForm

class FacultyRegistration(FormView):
    template_name = "user/faculty_registration.html"
    form_class = FacultyResgistrationForm
    success_url = '/login/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        user.set_password(user.password)
        user.save()
        return super().form_valid(form)