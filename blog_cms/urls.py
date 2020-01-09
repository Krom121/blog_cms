from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from blog.views import (ContactUsView, DashView, PostDetailView,
    PostListView, AboutView 
)
urlpatterns = [
    path('admin/', admin.site.urls),
    ## BLOG URLS
    path('', PostListView.as_view(), name='post-list'),
    path('post/<slug>/<pk>/', PostDetailView.as_view(), name='post-detail'),
    ## GENERIC URLS
    path('about_us/',AboutView.as_view(), name='about'),
    path('contact_us/', ContactUsView.as_view(), name='contactus'),
    ## AUTH URLS
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ## DABOARD URL
    path('dashboard/', DashView.as_view(), name='dashboard'),
    ## OTHER BASE URLS FOR DEPENDENCIES
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
