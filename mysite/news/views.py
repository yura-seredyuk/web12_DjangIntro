from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request,'news/post_list.html', {'posts':posts})


def post_details(request, pk):
    # post = Post.objects.filter(id=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request,'news/post_details.html', {'post':post})

