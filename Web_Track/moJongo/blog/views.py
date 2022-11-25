from django.shortcuts import render, HttpResponse
from .forms import BlogForm
from .models import Blog
# Create your views here.

def home(request):
    return HttpResponse('Home Page')

def create(request):
    create_blog_form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('Blog Published :)')
    return render(request, 'blog/create.html', {
        'form': create_blog_form,
    })

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/read.html', {
        'blogs': blogs
    })

def update(request, id):
    blog = Blog.objects.get(id=id)
    old_blog = BlogForm(instance=blog)
    if request.method == 'POST':
        new_blog = BlogForm(request.POST, instance=blog)
        if new_blog.is_valid():
            new_blog.save()
        return HttpResponse('Blog Update :)')
    return render(request, 'blog/update.html', {
        'form': old_blog
    })

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return HttpResponse('Blog Deleted :(')