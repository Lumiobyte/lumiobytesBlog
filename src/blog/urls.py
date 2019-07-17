from django.contrib import admin
from django.urls import path

from blog.views import blogPostDetail, blogPostList, blogPostCreate, blogPostUpdate, blogPostDelete

urlpatterns = [
    path('', blogPostList),
    path('<str:slug>/', blogPostDetail),

    path('<str:slug>/edit/', blogPostUpdate),
    path('<str:slug>/delete/', blogPostDelete)
]
