from typing import get_args
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Post, Comment
from .forms import CommentForm

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request , 'index.html' , context)


def details(request , pk):
    post = get_object_or_404(Post , pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('details' , pk=post.pk)

    form = CommentForm()
    context = {
        'post': post,
        'form': form
    }

    return render(request , 'details.html', context)