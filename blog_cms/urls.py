from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from blog.views import (ContactUsView, DashView, PostDetailView,
    PostListView, AboutView, CreateNew_post,
    UpdatePost, DeletePost
)
from rest_framework import routers, serializers, viewsets
from rest.views import (PostList, PostDetail, 
        CreatePost, UpdatePost, DeletePost

        )

urlpatterns = [
    path('batmans-admin/', admin.site.urls),
    
    ## BLOG URLS
    path('', PostListView.as_view(), name='post-list'),
    path('post/<slug>/<pk>/', PostDetailView.as_view(), name='post-detail'),
    ## GENERIC URLS
    path('about_us/',AboutView.as_view(), name='about'),
    path('contact_us/', ContactUsView.as_view(), name='contactus'),
    ## AUTH URLS
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ## DABOARD URL AND CRUD OPERATIONS
    path('dashboard/', DashView.as_view(), name='dashboard'),
    path('newpost/create', CreateNew_post.as_view()),
    path('update_post/<pk>/update', UpdatePost.as_view(), name='update_post'),
    path('delete_post/<pk>/delete', DeletePost.as_view(), name='delete_post'),
    #### REACT NATIVE ELECTRON API'S URLS MOBILE DEVELOPMENT #####
    path('post/', PostList.as_view(), name='post-list'),
    path('post/<slug>/<pk>/', PostDetail.as_view(), name='post-detail' ),
    path('post/create', CreatePost.as_view(), name='create-post'),
    path('post/<pk>/update', UpdatePost.as_view(), name='update-post'),
    path('post/<pk>/delete', DeletePost.as_view(), name='delete-post'),
    ## OTHER BASE URLS FOR DEPENDENCIES
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
