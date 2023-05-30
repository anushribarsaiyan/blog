from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from blogpp.models import *
from .serializers import Userserializer   , BlogSerializer
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
def index(request):
    return render(request,'app.html')



class StudentAPI(APIView):
   authentication_classes = [JWTAuthentication]
   permission_classes = [IsAuthenticated]

   def get(self,request,formate = None,pk= None):
      id = pk
      if id is not None:
        stu = PostModel.objects.get(id = id)
        serializer= BlogSerializer(stu)
        return Response(serializer.data)
       
      blog = PostModel.objects.all()
      serializer = BlogSerializer(blog,many = True)
      return Response(serializer.data)
    
   def post(self,request,formate = None,pk =None):
       serializer = BlogSerializer(data = request.data)
       if serializer.is_valid():
          serializer.save()
          return Response({"msg":"Data Created"})
       
   def put(self,request,pk=None,formate = None):
       id = pk
       blog = PostModel.object.get(id = id)
       blog_data = BlogSerializer(blog , data = request.data)
       return Response(blog_data)
    
   def delete(self,request,pk,fomate= None):
       id = pk
       stu = PostModel.objects.get(pk =id)
       stu.delete()
       return Response({"msg":"data delete"})

       
class RegisterUser(APIView):
   def post(self,request,formate = None,pk =None):
      serializer = Userserializer(data = request.data)

      if not serializer.is_valid():
         return Response({'status' :403,'error':serializer.errors,'mesage':'someting went wrong'})
      
      serializer.save()
      user = User.objects.get(username = serializer.data['username'])
      refresh = RefreshToken.for_user(user)
      return Response({ 
         'status':200,
         'payload': serializer.data,
         'refresh': str(refresh),
         'access': str(refresh.access_token),
         })
         
       