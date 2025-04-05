from django.shortcuts import render

from .models import BlogPost

# Create yourviews here.

def home(request):
    # get all blog posts objects
    posts = BlogPost.objects.all()

    message = "Welcome to Home Page this is a message"
    # context
    return render(request, 'index.html', {
        "message": message,
        "posts": posts
    })


def about(request):
    return render(request, 'about.html')

# contact view
