from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('mba', views.mba,name='mba'),
    path('admin/', admin.site.urls)
]
