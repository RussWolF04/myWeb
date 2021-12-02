from django.db import models


class Articles(models.Model):
    language = models.CharField('Язык программирования', max_length=20)
    intro = models.CharField('Вступление', max_length=250)
    article = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        return f'/training/{self.id}'

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'
