"""
URL configuration for Studious project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from notes.views import editor
# from notes.views import view_classes
# from notes.views import add_class

from notes import views

urlpatterns = [
    path("", include("notes.urls")),
    path('admin/', admin.site.urls),
    path('notes/', views.editor, name='editor'),
    path('classes/', views.view_classes,name='view_classes'),
    path('add_class/', views.add_class,name='add_class'),
    path('add_event/', views.add_event,name='add_event'),
    path('schedule/', include("schedule.urls")),
    path('meeting/', views.view_meeting_by_date, name='view_meeting_by_date'),
]
