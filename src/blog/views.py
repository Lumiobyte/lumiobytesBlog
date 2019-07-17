from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import BlogPostModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

def blogPostList(request):
    template = "blog/list.html"
    postQuerySet = BlogPost.objects.all()
    context = {"postObjList": postQuerySet}

    return render(request, template, context)

@staff_member_required
def blogPostCreate(request):
    template = "blog/create.html"

    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()

    context = {"form": form}

    return render(request, template, context)

def blogPostDetail(request, slug):
    template = "blog/detail.html"
    postObj = get_object_or_404(BlogPost, slug = slug)
    context = {"postObj": postObj}

    return render(request, template, context)

@staff_member_required
def blogPostUpdate(request, slug):
    template = "blog/update.html"
    postObj = get_object_or_404(BlogPost, slug = slug)

    form = BlogPostModelForm(request.POST or None, instance = postObj)

    if form.is_valid():
        form.save()

    context = {"postObj": postObj, "form": form}

    return render(request, template, context)

@staff_member_required 
def blogPostDelete(request, slug):
    template = "blog/delete.html"
    postObj = get_object_or_404(BlogPost, slug = slug)

    if request.method == "POST":
        postObj.delete()
        return redirect("/blog")

    context = {"postObj": postObj, "form": None}

    return render(request, template, context)