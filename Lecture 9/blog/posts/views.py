from django.shortcuts import render

# Create yourviews here.

def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

# contact view
