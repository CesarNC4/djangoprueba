from django.contrib import admin
from django.urls import path
from myapp.views import hello, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name='hello'),
    path('about/', about, name='about'),
]
