from rest_framework import serializers
from .models import Post

class JsonClass(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id","author","title","text","created_at")