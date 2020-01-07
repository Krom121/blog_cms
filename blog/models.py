from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from taggit.managers import TaggableManager

# BLOG RSS FEED MODEL

class Subscriber(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

### CONTACT FORM MODEL #######

class NewContact(models.Model):
    first_name = models.CharField(max_length=100,blank=True, null=True)
    Last_name = models.CharField(max_length=100,blank=True, null=True)
    email = models.EmailField(max_length=100,blank=True, null=True)
    company = models.CharField(max_length=100,blank=True, null=True)
    current_website = models.CharField(max_length=100,blank=True, null=True)
    tell_us_more = models.TextField()

    def __str__(self):
        return self.first_name

###### POST CREATOR MODEL ########

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image =  ProcessedImageField(upload_to='author_profile/',processors=[ResizeToFill(50, 50)],format='PNG',options={'quality': 60})

    def __str__(self):
        return self.user.username

##### POST BLOG CATEGORY MODEL ######

class Category(models.Model):
    title = models.CharField(max_length=30,blank=True,null=True)

    def __str__(self):
        return self.title

##### MAIN POST MODEL PUBLISHED MANAGER #######

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                          .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=100, blank=True,null=True)
    slug = models.SlugField(blank=True, null=True,unique_for_date='publish')
    author = models.ForeignKey(Author, on_delete=models.CASCADE,related_name='blog_posts')
    categories = models.ManyToManyField(Category)
    featured = models.BooleanField(default=False)
    tags = TaggableManager()
    image_thumbnail = ProcessedImageField(upload_to='thumnail_headers/',processors=[ResizeToFill(300, 350)],format='PNG',options={'quality': 60})
    blog_header_image = ProcessedImageField(upload_to='blog_headers/',processors=[ResizeToFill(750, 500)],format= 'PNG',options={'quality': 60})
    description = RichTextUploadingField(blank=True,null=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our published manager.

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={

            "slug": self.slug,
            "publish": self.publish,
            "tags": self.tags,
            "pk": self.pk, 
        
        })

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

##### POST COMMENT MODEL ######

class Comment(models.Model): 
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80,blank=True, null=True) 
    email = models.EmailField(max_length=150, blank=True, null=True) 
    your_comment = RichTextField(blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True) 
    updated = models.DateTimeField(auto_now=True) 
    active = models.BooleanField(default=True) 

    class Meta: 
        ordering = ('created',) 

    def __str__(self): 
        return 'Commented by {} on {}'.format(self.name, self.post)

##### AOUT PAGE MODEL ####

class AboutPage(models.Model):
    title = name = models.CharField(max_length=20,blank=True, null=True, unique=True)
    slug = models.SlugField(blank=True, null=True,unique=True)
    about_header_image = ProcessedImageField(upload_to='about_headers/',processors=[ResizeToFill(1200, 600)],format= 'PNG',options={'quality': 60})
    description = RichTextField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("page_detail", kwargs={
            
            "slug": self.slug
        })
    

    def __str__(self):
        return self.title
    