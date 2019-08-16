from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail

from blog.models import BlogPost

# if you want to do a .format in django in the html doc use {{valuename}} and then pass a disc in the render
# like this: {"valuename": "some value"} and it will substitute

def home_page(request):
    title = "Lumiobyte's Blog"
    postQuerySet = BlogPost.objects.all()[:3] # get only first 3 blog posts
    return render(request, "home.html", {"title": title, "blogPostList": postQuerySet})

def about_page(request):
    return render(request, "about.html", {})

def projects_page(request):
    return render(request, "projects.html", {})

def ads(request):
    content = 'google.com, pub-8076025812516606, DIRECT, f08c47fec0942fa0'
    return HttpResponse(content, content_type='text/plain')