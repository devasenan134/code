from django.shortcuts import render, HttpResponse
from .models import Blog
from .forms import BlogForm

# Create your views here.

def home(request):
    return HttpResponse("Home page !!")

def create(request):
    create_blog_form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Blog Created :)')
    return render(request, 'blog/create.html', {
        'form': create_blog_form
    })

def read(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/read.html', {
        'blogs': blogs
    })

def update(request, id):
    update_blog = Blog.objects.get(id=id)
    update_blog_form = BlogForm(instance=update_blog)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=update_blog)
        if form.is_valid():
            form.save()
            return HttpResponse('Blog Updated :)')
    return render(request, 'blog/update.html', {
        'form': update_blog_form
    })

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return HttpResponse('Blog Deleted :(')
    