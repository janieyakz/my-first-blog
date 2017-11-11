from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
def index(request):
    posts=Post.objects.all()
    context={'posts':posts}
    return render(request,'blog/post_list.html',context)
    
    
