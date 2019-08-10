from django.contrib import admin
from django.urls import path

from daysofcode.views import dayLogDetail, dayLogList, dayLogCreate, dayLogUpdate, dayLogDelete

urlpatterns = [
    path('', dayLogList),

    path('log/<int:id>/', dayLogDetail),

    path('log/<int:id>/edit', dayLogUpdate),
    path('log/<int:id>/delete', dayLogDelete),
]