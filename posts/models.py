from django.db import models
from django.db.models.base import Model
from django.db.models.fields import EmailField, SlugField

# Create your models here.
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.utils.text import slugify



class Post(models.Model):
    title = models.CharField(max_length=50)
    created_by = models.ForeignKey(User,  on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = SlugField(blank=True , null=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self , *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            return super(Post , self).save(*args, **kwargs)




class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments',  on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    """Model definition for Comment."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        return self.body
