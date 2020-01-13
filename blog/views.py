import requests
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.http import Http404
from django.views.generic.edit import FormMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import (TemplateView, FormView,

            ListView, DetailView, CreateView, 
            UpdateView, DeleteView
)
from .models import Post, AboutPage, Category
from .forms import SubscribeForm, CommentForm, ContactForm, NewPostForm

#### GENERIC VIEWS #####

class AboutView(TemplateView):
    model = AboutPage
    template_name = 'about_us/about.html'

    def get_context_data(self, **kwargs):
        form = ContactForm()
        context = super().get_context_data(**kwargs)
        context['title'] = 'About Us'
        context['form'] = form
        return context

class ContactUsView(TemplateView):
    queryset = Post.published.all()
    template_name = 'contact_us/contact.html'
    context_object_name = 'post'
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        form = ContactForm()
        featured = Post.published.filter(featured=True)
        latest = Post.published.order_by('-publish')[0:3]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact Us'
        context['featured'] = featured
        context['latest'] = latest
        context['form'] = form
        return context

#### AUTH VIEWS #####

class LoginView(TemplateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/login.html'

    def form_valid(self, form):
        view = super(LogIn, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view

##### DASHBOASRD VIEW ####

class DashView(TemplateView):
    model = Post
    
    template_name = 'dashboard/dashboard.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        featured = Post.published.filter(featured=True)
        latest = Post.published.order_by('-publish')[0:3]
        context = super().get_context_data(**kwargs)
        context['featured'] = featured
        context['latest'] = latest
        return context

#### CRUD OPERATIONS FOR DASHBOARD ######

class CreateNew_post(CreateView):
    form_class = NewPostForm
    queryset = Post.published.all()
    template_name = 'dashboard/create_post.html'
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        form = NewPostForm(data=request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)

class UpdatePost(UpdateView):
    model = Post
    template_name = 'dashboard/update_post.html'
    fields = ['title', 'slug', 'author', 'categories', 'description']
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        post = super(UpdatePost, self).get_object()

        return post 

class DeletePost(DeleteView):
    model = Post 
    template_name ='dashboard/delete_post.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        post = super(DeletePost, self).get_object()
        if not post.user == self.request.user:
            raise Http404
        return post

#### POST VIEWS MAIN LANDING PAGE ######

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'post'
    paginate_by = 1
    success_url = 'post-list'
    success_message = "You are now a subscriber Thank you"
    
   
    def post(self, request, *args, **kwargs):
        form = SubscribeForm(data=request.POST)
        if form.is_valid():
            form.save()
        return self.get(request, *args, **kwargs)
    


    def get_context_data(self, **kwargs):
        form = SubscribeForm()
        post = Post.published.all()[0:6]
        featured = Post.published.filter(featured=True)
        latest = Post.published.order_by('-publish')[0:4]
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome'
        context['category'] = Category.objects.filter()
        context['post'] = post
        context['featured'] = featured
        context['latest'] = latest
        context['form'] = form
        return context



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        form = CommentForm()
        context = super().get_context_data(**kwargs)
        context['form'] = form
        return context
    
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post-detail", kwargs={
                'pk': post.pk
            }))