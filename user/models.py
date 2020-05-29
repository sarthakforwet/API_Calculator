# from django.db import models
# from api.models import CategoryStream 
# from django.contrib.auth.models import User

# Create your models here.
# class FacultyProfile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     stream_choices = [
#         ('', '----'),
#         ('FOLA/H/SS/L/PEM','Faculties of Languages Arts/Humanities/Social Sciences/Library/Physical education/Management'),
#         ('E/A/VS/S/MS','Engineering/Agriculture/Veterinary Science/Sciences/Medical Sciences')
#     ]
#     stream = models.CharField(max_length=60,choices=stream_choices)
#     def __str__(self):
#         return str(self.user.username)

