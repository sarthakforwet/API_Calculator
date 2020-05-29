from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return str(self.category_name)

class CategoryStream(models.Model):
    category_id = models.ForeignKey(Category,on_delete=models.CASCADE)
    stream = models.CharField(max_length=500)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['category_id', 'stream'],name='category_stream')
        ]
    def __str__(self):
        return str(self.stream)


class Api(models.Model):
    stream = models.ForeignKey(CategoryStream,on_delete=models.CASCADE)
    nature_of_activity = models.CharField(max_length=750)
    max_score = models.PositiveSmallIntegerField()
    self_assesment = models.PositiveSmallIntegerField(default=None,null=True,blank=True)
    verified_api_score = models.PositiveSmallIntegerField(default=None,null=True,blank=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['nature_of_activity', 'stream'],name='api')
        ]
    def __str__(self):
        return str(self.nature_of_activity)
