from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post

# Create your views here.
def index(request):
    # return HttpResponse("Hello Universe, you are at blog's Index")
    blog_title = "Latest Posts"
    # posts = [
    #     {'id': 1, 'title': 'Post 1', 'content': 'Content for Post 1'},
    #     {'id': 2, 'title': 'Post 2', 'content': 'Content for Post 2'},
    #     {'id': 3, 'title': 'Post 3', 'content': 'Content for Post 3'},
    #     {'id': 4, 'title': 'Post 4', 'content': 'Content for Post 4'},
    # ]
    posts = Post.objects.all()
    return render(request, "index.html", {'blog_title': blog_title, 'posts': posts})

# def detail(request, post_id):
def detail(request, slug):
    # return HttpResponse("Hello Universe, you are at blog's Index")
    # post = Post.objects.get(pk=post_id)
    post = Post.objects.get(slug=slug)

    return render(request, "detail.html", {'post': post})

# def detail(request, post_id):
#     return HttpResponse(f"You are viewing Post details page of post-id - {post_id}")

def old_url_redirect(request):
    return redirect(reverse("blog:new_url"))

def new_url_redirect(request):
    return HttpResponse("You are viewing New URL")