from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView  # встроенный метод для создания Динамических листов


def training_home(request):
    training = Articles.objects.all()
    return render(request, 'training/training_home.html', {'training': training})


class TrainingDetailView(DetailView):  # Класс для того что бы читать всю статью целиком
    model = Articles
    template_name = 'training/details_view.html'  # Указываем какой шаблон будет обрабатывать страницу
    context_object_name = 'training'


class TrainingUpgradeView(UpdateView):  # Для редактирования базы данных статьи
    model = Articles
    template_name = 'training/update.html'
    form_class = ArticlesForm


def update(request):
    # Переменная для созранения ошибок при заполнении формы добавления языка программирования
    error = ''
    # Проверка метода передачи данных на то что они идут из формы POST
    if request.method == 'POST':
        # Получение из формы от пользователя
        form = ArticlesForm(request.POST)
        # Проверка на корректно заполнение полей методом из ModelForm
        if form.is_valid():
            # Сохраняем донные из формы если форма заполнена верно
            form.save()
            # если все верно то переходим после добавления на страницу с языками программирования
            return redirect('training_home')
        else:
            # если заполнение было не верным то выдас сообщение об этом
            error = 'Форма заполнения была не верной'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'training/update.html', data)