from django.contrib import admin
from blogpp.models import *

# Register your models here.

@admin.register(PostModel)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["id" , "tittle" ,"body","author"]
