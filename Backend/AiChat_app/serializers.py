from AiChat_app.models import Chat, ChatMessage
from rest_framework import serializers


class ChatSerializer(serializers.ModelSerializer):
   
   class Meta:
       model = Chat
       fields = "__all__"


# class ChatMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatMessage 
#         fields = ["id", "role", "content", "created_at"]


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage 
        fields = ["role", "content"]
        