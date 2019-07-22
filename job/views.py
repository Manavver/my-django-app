from django.shortcuts import render

from .models import Post

def index(request):
    jobs = Post.objects.all()
    return render(request, 'job/index2.html', {'jobs': jobs})