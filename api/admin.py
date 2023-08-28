from django.contrib import admin

# Register your models here.
# admin.py

from django.contrib import admin

from api.models import Student

admin.site.register(Student)
