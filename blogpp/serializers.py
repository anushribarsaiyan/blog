from rest_framework import serializers
from .models import PostModel
from django.contrib.auth.models import User



class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password']


    def create(self, validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields =['id','tittle','body', 'author']

