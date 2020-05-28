from django.contrib import admin
from api.models import Category, CategoryStream, Api
# Register your models here.
admin.site.register(Category)
admin.site.register(CategoryStream)
admin.site.register(Api)