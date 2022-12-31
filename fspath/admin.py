from django.contrib import admin
from .models import Student  # model.py dosyasından Student modelini import ederiz

admin.site.register(Student)
