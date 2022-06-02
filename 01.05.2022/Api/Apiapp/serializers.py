from rest_framework import serializers
from .models import Mailing_list, Custom, Message


class Mailing_listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing_list
        fields = ('text_message', 'custom')

class CustomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Custom
        fields = ('number', 'code', 'tag', 'hour')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('date_create', 'status', 'user', 'mailing_list')


