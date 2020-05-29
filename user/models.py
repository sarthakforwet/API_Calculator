from django.db import models
from django.contrib.auth.models import User
from api.models import Api
# Create your models here.
class FacultyProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    stream_choices = [
        ('', '----'),
        ('FOLA/H/SS/L/PEM','Faculties of Languages Arts/Humanities/Social Sciences/Library/Physical education/Management'),
        ('E/A/VS/S/MS','Engineering/Agriculture/Veterinary Science/Sciences/Medical Sciences')
    ]
    stream = models.CharField(max_length=30,choices=stream_choices)
    def __str__(self):
        return str(self.user.username)

class FacultyApi(models.Model):
    user = models.ForeignKey(FacultyProfile,on_delete=models.CASCADE)
    nature_of_activity = models.ForeignKey(Api,on_delete=models.CASCADE)
    self_assesment = models.PositiveSmallIntegerField(default=None,null=True,blank=True)
    verified_api_score = models.PositiveSmallIntegerField(default=None,null=True,blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nature_of_activity', 'user'],name='faculty_api')
        ]
    def __str__(self):
        return str(self.user)