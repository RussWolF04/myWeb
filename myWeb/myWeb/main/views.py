from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView


def index(request):
    data = {
        'title': 'IT_OverOne',
    }
    return render(request, 'main/index.html', data)


def training(request):
    return render(request, 'main/training.html')


def contacts(request):
    return render(request, 'main/contacts.html')
