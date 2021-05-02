from rest_framework import generics 
from .models import Post
from .serializers import JsonClass

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = JsonClass

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = JsonClass
    

