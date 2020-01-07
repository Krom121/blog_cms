from django.contrib import admin
from .models import Subscriber,Post,Category,Comment,NewContact,Author,AboutPage

admin.site.register(Subscriber)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(NewContact)
admin.site.register(Author)
admin.site.register(AboutPage)