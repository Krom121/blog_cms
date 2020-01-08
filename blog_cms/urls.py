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
    path('', PostListView.as_view(), name='post-list'),
    path('about_us/',AboutView.as_view(), name='about'),
    path('contact_us/', ContactUsView.as_view(), name='contactus'),
    ## AUTH URLS
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', DashView.as_view(), name='dashboard'),
     path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
