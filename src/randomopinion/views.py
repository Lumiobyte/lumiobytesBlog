from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Opinion
from .forms import OpinionModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings


def createOpinion(request):
   template = "randomopinion/create.html"
   
   form = OpinionModelForm(request.POST or None)
   if form.is_valid():
    obj = form.save(commit=False)
    obj.likes = 0
    obj.save()
    form = OpinionModelForm()

   return render(request, template, {'form': form})

def viewOpinion(request):
    template = "randomopinion/detail.html"

    OpinionList = Opinion.objects.all()
    p = Paginator(OpinionList, 1)

    page = request.GET.get('p')

    OpinionObjPage = p.get_page(page)

    if request.method == "POST":
        for OpinionObj in OpinionObjPage:
            temp = OpinionObj
            temp.likes = temp.likes + 1
            temp.save()

    return render(request, template, {'OpinionObjPage': OpinionObjPage})