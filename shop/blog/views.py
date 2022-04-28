from tempfile import template
from datetime import datetime
from django.shortcuts import get_object_or_404, render,get_list_or_404
from django.http import HttpResponse,Http404
from .models import Post
from django.views.decorators.http import require_http_methods,require_GET,require_safe
# Create your views here.

@require_http_methods(["GET"])
def index(Request):
    lates_posts_list = Post.objects.order_by('publish')[:5]

    context ={
        'lates_posts_list':lates_posts_list,
    }
    return render(Request,'index.html',context)

@require_GET
def detail(Request,post_id):

    post = get_object_or_404(Post, pk = post_id)
    
    context = {
        'post':post,
    }

    return render(Request,'detail.html',context)

@require_safe
def archive_year(request,year):
    year_archive_posts = get_list_or_404(Post,publish__year=year) 
    # Post.objects.filter(publish__year= year)
    context = {
        'year_archive_posts':year_archive_posts,
    }
    return render (request,'archive.html',context)


