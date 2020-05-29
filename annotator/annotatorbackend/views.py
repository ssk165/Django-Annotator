from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Annotation, CharacterSet
from .serializers import AnnotationSerializer, UserSerializer, CharacterSetSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )


class CharacterSetSerializer(viewsets.ModelViewSet):
    queryset = CharacterSet.objects.all()
    serializer_class = CharacterSetSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
