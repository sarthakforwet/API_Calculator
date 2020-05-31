from django.contrib import admin
from api.models import Category, CategoryStream, Api, FacultyProfile, FacultyApi
# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryStream)
admin.site.register(Api)
admin.site.register(FacultyProfile)
admin.site.register(FacultyApi)