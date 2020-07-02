from django.contrib import admin
from .models import Post, user, Comment
from django.contrib.auth.models import User

class userAdmin(admin.ModelAdmin):
    fields = ['username','firstname','lastname','Email']
admin.site.register(user,userAdmin)

class PostAdmin(admin.ModelAdmin):
    fields = ['Title','User','Content']
admin.site.register(Post,PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    fields = ['User_Comment','Postuser','Content','Post']
admin.site.register(Comment,CommentAdmin)
