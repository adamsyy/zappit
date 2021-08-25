from django.contrib.auth.models import Permission
from .serializers import PostSerializer
from posts.models import Post
from django.shortcuts import render
from rest_framework import generics,permissions
from .models import Post
# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(poster=self.request.user)


