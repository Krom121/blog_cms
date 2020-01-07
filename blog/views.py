from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import SubscribeForm, CommentForm, ContactForm


class HomeView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about_us/about.html'

class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact_us/contact.html'
    success_url = reverse_lazy('home')

    ### FROM LOGIC ###
    def form_invalid(self, form):
        form.save()
        return super(ContactView, self).form_invalid(form)

class LoginView(TemplateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('dashboard')
    template_name = 'registration/login.html'

class DashView(TemplateView):
    template_name = 'dashboard/dashboard.html'

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    template_name = 'blog/list.html'

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
        post_tags_ids = post.tags.values_list('id', flat=True)
        similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
        similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:4]
    return render(request, 'blog/posts/detail.html', {'post': post, 'comments': comments,
                   'new_comment': new_comment,
                   'comment_form': comment_form, 'similar_posts': similar_posts})
    

 
    