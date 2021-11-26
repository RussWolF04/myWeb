from django.shortcuts import render


def index(request):
    data = {
        'title': 'IT_OverOne',
    }
    return render(request, 'main/index.html', data)


def python(request):
    return render(request, 'main/python.html')
