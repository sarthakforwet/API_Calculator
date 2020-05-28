from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)

class CategoryStream(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    stream = models.CharField(max_length=500)

class Api(models.Model):
    stream = models.ForeignKey(CategoryStream,on_delete=models.CASCADE)
    nature_of_activity = models.CharField(max_length=750)
    max_score = models.PositiveSmallIntegerField()
    self_assesment = models.PositiveSmallIntegerField()
    verified_api_score = models.PositiveSmallIntegerField()
