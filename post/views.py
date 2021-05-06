from rest_framework import viewsets
from .models import Post
from .serializers import JsonClass, UserJsonClass
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = JsonClass
    

class UserList(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserJsonClass
