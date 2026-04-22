from django.contrib import admin
from django.urls import path
from . import views
from myapp.views import hello, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('project/', views.project, name='project'),
    path('task/', views.task, name='tasks'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_projects/', views.create_projects, name='create_projects'),
]
