import requests
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template import loader

from catdog.forms import SearchForm, SPECIES_CHOICES, TYPES_CHOICES, SendEmailForm
from catdog.models import AnimalImage


def home(request):
    return render(request, 'home.html', {'form': SearchForm()})


def get_cat_url():
    data = requests.get('https://aws.random.cat/meow').json()
    return data['file']


def get_dog_url():
    data = requests.get('https://dog.ceo/api/breeds/image/random').json()
    return data['message']


def get_image(request):
    if request.method == 'POST':
        button = request.POST['button']
        if button == 'I love cats!':
            link = get_cat_url()
            species = 'Cat'
        elif button == 'I love dogs!':
            link = get_dog_url()
            species = 'Dog'
        extension = link.split('.')[-1]

        animal_image_data = dict(
            url=link,
            type=extension,
            species=species,
        )
        request.session['animal_image_data'] = animal_image_data
        return render(request, 'get_image.html', {'image': link})
    return redirect(home)


def save_image(request):
    if request.method == 'POST' and 'animal_image_data' in request.session:
        animal_image_data = request.session['animal_image_data']
        AnimalImage.objects.create(**animal_image_data)
        return redirect('send-image')
    return redirect(home)


def send_image(request):
    if 'animal_image_data' in request.session:
        if request.method == 'GET':
            context = {
                'image': request.session['animal_image_data']['url'],
                'send_form': SendEmailForm(),
            }
            return render(request, 'send_image.html', context)
        else:
            form = SendEmailForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                html_message = loader.render_to_string(
                    'email.html', {'image': request.session['animal_image_data']['url']},
                )
                send_mail(
                    subject=cd['topic'],
                    message='',
                    html_message=html_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[cd['receiver']],
                    fail_silently=False,
                )
    return redirect('home')


def filter_images(request):
    if request.method == 'POST':
        data = SearchForm(request.POST)
        if data.is_valid():
            cleaned_data = data.cleaned_data
            species_search = cleaned_data.get('species')
            type_search = cleaned_data.get('type')

            species = dict(SPECIES_CHOICES).get(species_search)
            image_type = dict(TYPES_CHOICES).get(type_search)
            animals = AnimalImage.objects.filter(species=species, type=image_type.lower())
            return render(request, 'search_result.html', {'animals': animals})
    return redirect(home)
