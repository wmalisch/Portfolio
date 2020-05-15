from django.shortcuts import render, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-date')[:7]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})

def detail(request, blog_id):
    # first param is the object we are looking for
    # second param is the primary key
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html',{'blog':blog})