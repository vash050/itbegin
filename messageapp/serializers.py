from django.conf import settings
from django.forms import DateField
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from authapp.models import SiteUser
from messageapp.models import Dialog, Message


class DialogSerializer(ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['members', 'last_message', 'objects']


class UserSerializer(ModelSerializer):
    class Meta:
        model = SiteUser
        fields = ['first_name', 'last_name', 'id', 'username']  # оставить только username


class MessageSerializer(ModelSerializer):
    user_name = serializers.CharField(source="author.username", read_only=True)
    user_avatar = serializers.ImageField(source="author.avatar", read_only=True)
    all_members = UserSerializer(source="dialog.members", many=True, read_only=True)

    class Meta:
        model = Message
        fields = ['dialog', 'all_members', 'author', 'user_name', 'user_avatar', 'message', 'pub_date', 'is_read',
                  'is_active']
