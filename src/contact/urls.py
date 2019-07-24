from django.urls import path, include

from contact.views import contact_page, contact_requests, view_request, del_request

urlpatterns = [

    path('', contact_requests),

    path('<int:id>/', view_request),
    path('<int:id>/delete', del_request)
]
