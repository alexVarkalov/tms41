from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader


def index(request):
    now = datetime.now()
    return HttpResponse(str(now))


def two_pow(request, number):
    result = 2 ** number
    return HttpResponse(str(result))


def my_word(request, word):
    if len(word) % 2 == 0:
        return HttpResponse(word[::2])
    return redirect('index')


def user_form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        result = f'{firstname}-{lastname}-{age}\n'
        with open('users.txt', 'a') as write_file:
            write_file.write(result)
        return HttpResponse('Saved!')
    return HttpResponse('Wrong Method', status=405)


def form(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        result = f'{firstname}-{lastname}-{age}\n'
        with open('users.txt', 'a') as write_file:
            write_file.write(result)
        return HttpResponse('Saved!')
    elif request.method == "GET":
        template = loader.get_template('user_form.html')
        response = template.render({}, request)
        return HttpResponse(response)
    return HttpResponse('Wrong Method', status=405)
