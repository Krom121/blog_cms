from django.urls import path
from django.contrib.auth import views as auth_views
from blog import views

app_name = 'blog'

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('about_us/',views.AboutView.as_view(), name='about'),
    ## AUTH URLS
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.DashView.as_view(), name='dashboard'),
    path('blog/', views.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]
