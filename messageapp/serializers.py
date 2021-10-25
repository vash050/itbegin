from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from messageapp.models import Dialog, Message


class DialogSerializer(ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['members', 'last_message', 'objects']


class MessageSerializer(ModelSerializer):
    user_name = serializers.CharField(source="author.username")
    user_avatar = serializers.ImageField(source="author.avatar")

    class Meta:
        model = Message
        fields = ['dialog', 'author','user_name','user_avatar', 'message', 'pub_date', 'is_read', 'is_active']
