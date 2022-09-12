from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)
    return render(request,'news/post_list.html', {'posts':posts})


def post_details(request, pk):
    # post = Post.objects.filter(id=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request,'news/post_details.html', {'post':post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk = post.pk)
    else:
        form = PostForm(instance=post)
    return render(request,'news/post_edit.html', {'form':form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')

