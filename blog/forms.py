from django import forms
from .models import Subscriber, Comment, NewContact

#### SUBCRIBER FORM #######

class SubscribeForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = Subscriber
        fields = ('name','email')

##### CONTACT FORM #######

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    tell_us_more = forms.Textarea()

    class Meta:
        model = NewContact
        fields = ('first_name','last_name','email','tell_us_more')

##### POST COMMENT FORM #####

class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    your_comment = forms.Textarea()

    class Meta:
        model = Comment
        fields = ('name', 'email', 'your_comment')
