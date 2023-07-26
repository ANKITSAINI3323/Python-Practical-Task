# from django.shortcuts import render
# from .models import User
# from rest_framework.decorators import api_view
# from .serializers import UserSerializers,PostSerializer,LikeSerializer
# from rest_framework.response import Response
# from rest_framework import status 

# # Create your views here.
# # fetch all records from models 
# @api_view(['GET'])
# def getallUserData(request):
#     user = User.objects.all() 
#     us = UserSerializers(user,many=True)
#     print("======>>>>us ",us)
#     print("======>>>>us ",us.data)
#     return Response(us.data)

# @api_view(['GET'])
# def myData(request):
#     data = User.objects.all() 
#     if data:
#         serializer = UserSerializers(data,many=True)
#         return Response(serializer.data)
    
# @api_view(['GET'])  # get specific id wise data 
# def getSpecificUser(request,id):
#     data = User.objects.get(id = id) 
#     if data:
#         serializer = UserSerializers(data)
#         return Response(serializer.data)
    
# @api_view(['POST'])  # store data in model
# def userAdd(request):
#     userData = UserSerializers(data = request.data)
#     if userData.is_valid():
#         userData.save() 
#         return Response(userData.data)
#     else:
#         return Response(status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','PUT'])   
# def userUpdate(request,id):
#     user_id = User.objects.get(id = id)
#     userSerial = UserSerializers(data = request.data,instance=user_id)
#     if userSerial.is_valid():
#         if request.method=="PUT":
#             userSerial.save()
#             return Response(userSerial.data)
#         else:
#             return Response(status = status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET','DELETE'])   
# def userDelete(request,id):
#     user= User.objects.get(id = id)
#     if request.method == "GET":
#         userSerial = UserSerializers(user)
#         return Response(userSerial.data)
#     if request.method == "DELETE":
#         User.delete(user) 
#         return Response(status= status.HTTP_202_ACCEPTED)
#     else:
#         return Response(status= status.HTTP_404_NOT_FOUND)

    

# views.py
from rest_framework import generics
from .models import User, Post, Like
from .serializers import UserSerializers, PostSerializer, LikeSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
