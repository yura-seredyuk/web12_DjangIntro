from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm, LoginForm


def post_list(request):
    # posts = Post.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # return HttpResponse('Authenticated successfully!')
                    return redirect('post_list')
                else:
                    return HttpResponse('Disabled account!')
            else:
                return HttpResponse('Invalid username or password!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})


def user_logout(request):
    logout(request)
    return redirect('post_list')


def user_signin(request):
    if request.method == 'POST':
        user = {"username": request.POST["username"],
                "password": request.POST["password"],
                "email": request.POST["email"]}
        created_user = User.objects.create_user(**user)
        return redirect('login')
    return render(request, 'register.html')
