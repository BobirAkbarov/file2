from rest_framework import generics, viewsets
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Mailing_list, Message, Custom
from .serializers import Mailing_listSerializer, MessageSerializer, CustomSerializer


class UserListView(generics.ListAPIView):
    ...
    filter_backends = [DjangoFilterBackend]

class Mailing_listAPIView(generics.ListAPIView):
    queryset = Mailing_list.objects.all()
    serializer_class = Mailing_listSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['text_message', 'custom']



class CustomAPIView(generics.ListAPIView):
    queryset = Custom.objects.all()
    serializer_class = CustomSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['number', 'code', 'tag', 'hour']



class MessageAPIView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_create', 'status', 'user', 'mailing_list']



