import blog.views
from django.contrib.auth.models import User 
from rest_framework import serializers
from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title', 'slug', 'author',
                  'featured','categories', 
                  'description', 'image_thumbnail',
                  'blog_header_image', 'publish',
                  'status', 'created', 'published'
  
                    
                )