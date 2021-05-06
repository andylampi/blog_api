from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

class JsonClass(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","author","title","text","created_at")


class UserJsonClass(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id","username")