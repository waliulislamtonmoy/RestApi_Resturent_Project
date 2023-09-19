from django.shortcuts import render
from rest_framework import parsers
from rest_framework.viewsets import ModelViewSet
from App_Account.models import User
from App_Account.serializer import UserSerializer


class UserViewsets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [parsers.FormParser,
                      parsers.MultiPartParser, parsers.JSONParser]
