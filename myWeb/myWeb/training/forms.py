from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['language', 'intro', 'article', 'date']

        widgets = {
            'language': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Название языка"
            }),
            'intro': TextInput(attrs={
                'class': "form-control",
                'placeholder': "Краткое описание"
            }),
            'article': Textarea(attrs={
                'class': "form-control",
                'placeholder': "Текст описания языка"
            }),
            'date': DateTimeInput(attrs={
                'class': "form-control",
                'placeholder': "Дата побликации"
            }),
        }