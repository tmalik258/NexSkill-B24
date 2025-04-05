from django.shortcuts import render

from .models import BlogPost

# Create yourviews here.

def home(request):
    # get all blog posts objects
    # posts = BlogPost.objects.filter(body__icontains="This")
    posts = BlogPost.objects.all()

    message = "Welcome to Home Page this is a message"
    # context
    return render(request, 'index.html', {
        "message": message,
        "posts": posts
    })


def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id) # to get a single object

    return render(request, 'post_detail.html', {
        "post": post,
    })


def about(request):
    return render(request, 'about.html')

# contact view
