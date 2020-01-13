from django.forms import ModelForm
from .models import Subscriber, Comment, NewContact, Post

#### SUBCRIBER FORM #######

class SubscribeForm(ModelForm):

    class Meta:
        model = Subscriber
        fields = ('name','email')

##### CONTACT FORM #######

class ContactForm(ModelForm):

    class Meta:
        model = NewContact
        fields = ('first_name','last_name','email','tell_us_more')

##### POST COMMENT FORM #####

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'your_comment')

class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author',
                'featured','categories', 
                'description', 'image_thumbnail',
                'blog_header_image', 'publish',
                'status'
)