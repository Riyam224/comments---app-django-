from django.contrib import admin
from django.utils import regex_helper

# Register your models here.
from .models import Post , Comment

admin.site.register(Post)
admin.site.register(Comment)