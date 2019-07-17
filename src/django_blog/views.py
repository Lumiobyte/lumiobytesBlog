from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from blog.models import BlogPost

# if you want to do a .format in django in the html doc use {{valuename}} and then pass a disc in the render
# like this: {"valuename": "some value"} and it will substitute

def home_page(request):
    title = "Lumiobyte's Blog"
    postQuerySet = BlogPost.objects.all()[:3] # get only first 3 blog posts
    return render(request, "home.html", {"title": title, "blogPostList": postQuerySet})

def about_page(request):
    title = "Abt ((about)) Abt Us"
    return render(request, "about.html", {"title": title})

def contact_page(request):
    title = "Contact Us"

    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(form.cleaned_data)

    return render(request, "contactForm.html", {"title": title, "form": form})