from django.shortcuts import render, get_object_or_404
from .models import Post


def blog_index(request):
    posts = Post.objects.all()
    return render(request, 'blog/blog.html', {'posts':posts})

def post_detail(request, id, slug):
    post = get_object_or_404(Post, id=id, slug=slug)
    return render(request, 'blog/post-detail.html', {'post': post})
