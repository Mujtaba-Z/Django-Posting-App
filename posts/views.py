from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def posts_list(request):
    posts = Post.objects.all().order_by('-date') ### Gets all posts ordered by date
    return render(request, 'posts/posts_list.html', {'posts': posts}) ### Pulls from its 'templates' directory. Input 'posts' is posts variable, which is list of posts

def post_page(request, slug):
    post = Post.objects.get(slug=slug) ### Gets the post with the matching slug
    return render(request, 'posts/post_page.html', {'post': post}) ### Pulls from its 'templates' directory

@login_required(login_url='/users/login/') ### Checks if user is logged in. If not, they are redirected to the login_url variable address (/users/login/)
def post_new(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES) ### Sending in post detials and files (image)
        if form.is_valid(): ### Checking if what was submitted is valid against the model
            # save with user
            newpost = form.save(commit=False) ### New instance of post
            newpost.author = request.user
            newpost.save()
            return redirect('posts:list')
    else:
        form = forms.CreatePost()
    return render(request, 'posts/post_new.html', { "form": form })