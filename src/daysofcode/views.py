from django.shortcuts import render, get_object_or_404, redirect

from .models import DayLog
from .forms import DayLogModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings

def dayLogList(request):
    template = "daysofcode/list.html"
    logQuerySet = DayLog.objects.all()
    mostRecentLog = DayLog.objects.all()[:1]
    context = {"logObjList": logQuerySet, "mostRecentLog": mostRecentLog, "test": "lpol"}

    return render(request, template, context)

@staff_member_required
def dayLogCreate(request):
    template = "daysofcode/create.html"

    form = DayLogModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = DayLogModelForm()

    context = {'form': form}

    return render(request, template, context)

def dayLogDetail(request, id):
    template = 'daysofcode/detail.html'
    logObj = get_object_or_404(DayLog, id = id)
    context = {'logObj': logObj}

    return render(request, template, context)

@staff_member_required
def dayLogUpdate(request, id):
    template = 'daysofcode/edit.html'
    logObj = get_object_or_404(DayLog, id = id)

    form = DayLogModelForm(request.POST or None, instance = logObj)

    if form.is_valid():
        form.save()

    context = {'logObj': logObj, 'form': form}

    return render(request, template, context)

@staff_member_required
def dayLogDelete(request, id):
    template = 'daysofcode/delete.html'
    logObj = get_object_or_404(DayLog, id = id)

    if request.method == 'POST':
        logObj.delete()
        return redirect('/100daysofcode')

    context = {'logObj': logObj, 'form': None}

    return render(request, template, context)
