from django.shortcuts import render
from rest_framework import generics

from .serializers import UserSerializer
from django.contrib.auth.models import User
# is a permission class that checks if the user is authenticated
from rest_framework.permissions import IsAuthenticated
# Middleware for authentication, they intercept the request and check if the user is authenticated
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)

# JWTAuthentication is a class that provides authentication using JSON Web Tokens

from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # This part is for authentication and permission classes that are used to check if the user is authenticated and has permission to access the view
    # authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    # authentication_classes = [TokenAuthentication]
    # 
    authentication_classes = [JWTAuthentication]
    # This part is for permission classes that are used to check if the user is authenticated and has permission to access the view using JWT
    permission_classes = [IsAuthenticated]