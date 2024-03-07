from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

class PostList(generic.ListView):
    # model = Post
    # queryset = Post.objects.all().order_by("-created_on") #this will display all db posts in descending order (newest to oldest)
    # queryset = Post.objects.filter(author=1)
    queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"