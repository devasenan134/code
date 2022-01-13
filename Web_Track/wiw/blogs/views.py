from django.shortcuts import render
from home.models import Video


# Create your views here.
def blogs(request):
    data = Video.objects.order_by('-date')[:5]
    count = Video.objects.count
    return render(request, "blogs/blogs.html", {
        "blogs": data,
        "count": count
    })

def blog(request, blog_id):
    blog = Video.objects.get(id=blog_id)
    return render(request, "blogs/blog.html", {
        "blog": blog
    })