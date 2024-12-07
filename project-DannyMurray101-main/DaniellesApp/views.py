from datetime import datetime

from django.contrib.auth.decorators import login_required

from .models import Post

# Create your views here.
from django.http import HttpResponse

posts = [
    {
        'author': 'BigTim',
        'title': 'do NOT go to money bay',
        'content': 'I saw a goblin in the Mooneys Bay popeyes',

    }
]

def hello_world(request):
    return HttpResponse("Hello World!")
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'index.html', context)

@login_required
def create_post(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content, author=request.user)
        return redirect('index')
    return render(request, 'create_post.html')