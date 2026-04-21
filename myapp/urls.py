from django.contrib import admin
from django.urls import path
from . import views
from myapp.views import hello, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('hello/<str:name>/', views.hello),
    path('project/<int:project_id>/', views.project),
    path('task/<int:task_id>/', views.task),
    path('create_task/', views.create_task, name='create_task'),
]
