from rest_framework import viewsets
from .models import Post
from .serializers import JsonClass, UserJsonClass
from .permissions import IsAuthorOrReadOnly, IsUser
from django.contrib.auth import get_user_model

class PostList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = JsonClass
    

class UserList(viewsets.ModelViewSet):
    permission_classes = (IsUser, )
    queryset = get_user_model().objects.all()
    serializer_class = UserJsonClass
