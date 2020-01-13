from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework.reverse import reverse 
from rest_framework import filters
from rest_framework import generics
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import PostSerializer
from blog.models import Post


##### REACT NATIVE ELECTRON API'S MOBILE DESKTOP APP ######

class PostList(generics.ListAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    name = 'post-list'

class PostDetail(generics.RetrieveAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    name = 'post-detail'

class CreatePost(CreateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class UpdatePost(UpdateAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer

class DeletePost(DestroyAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer