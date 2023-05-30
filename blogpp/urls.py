from django.contrib import admin
from django.urls import path,include
from blogpp import views


urlpatterns = [
    path('studentapi',views.StudentAPI.as_view()),
    path('studentapi/<int:pk>',views.StudentAPI.as_view()),
    path('register/',views.RegisterUser.as_view())
   
]