from rest_framework.serializers import ModelSerializer

from messageapp.models import Dialog, Message


class DialogSerializer(ModelSerializer):
    class Meta:
        model = Dialog
        fields = ['members', 'last_message', 'objects']


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['dialog', 'author', 'message', 'pub_date', 'is_read', 'is_active']
