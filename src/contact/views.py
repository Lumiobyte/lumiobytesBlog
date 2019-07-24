from django.shortcuts import render, get_object_or_404, redirect

from .models import ContactRequests
from .forms import ContactModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings


def contact_page(request):
    title = "Contact Us"

    didSucceed = False

    form = ContactModelForm(request.POST or None)

    if form.is_valid():
        didSucceed = True
        obj = form.save()
        form = ContactModelForm()

        print(didSucceed)

    print(didSucceed)

    return render(request, "contact/contactForm.html", {"title": title, "form": form, "success": didSucceed})

@staff_member_required
def contact_requests(request):
    template = "contact/contactRequests.html"
    contactQuerySet = ContactRequests.objects.all()
    context = {"contactObjList": contactQuerySet}

    return render(request, template, context)

@staff_member_required
def view_request(request, id):
    template = "contact/requestDetail.html"
    contactObj = get_object_or_404(ContactRequests, id = id)
    context = {"contactObj": contactObj}

    return render(request, template, context)

@staff_member_required 
def del_request(request, id):
    template = "contact/requestDelete.html"
    postObj = get_object_or_404(ContactRequests, id = id)

    if request.method == "POST":
        postObj.delete()
        return redirect("/contactRequests")

    context = {"postObj": postObj, "form": None}

    return render(request, template, context)
