# from rest_framework import serializers
# from .models import * 

# class UserSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = UserInfo
#         fields = ("id","name","city","email","mobile")
        
#     # name = serializers.CharField(max_length=30)
#     # city = serializers.CharField(max_length=30)
#     # email = serializers.EmailField()
#     # mobile = serializers.CharField(max_length=30) 

#     # def create(self,validated_data):
#     #     return UserInfo.objects.create(**validated_data)

#     # def update(self, instance, validated_data):
#     #     instance.select_campus = validated_data["id"]
#     #     instance.save()
#     #     return instance

from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
