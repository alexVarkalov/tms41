"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from app1.views import index, two_pow, my_word, user_form, form

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('two_pow/<int:number>', two_pow, name='two-pow'),
    path('my_word/<str:word>', my_word, name='my-word'),
    path('user_form/', user_form, name='user-form'),
    path('form/', form, name='form'),
    path('catdog/', include('catdog.urls')),
]
