"""
Definition of models.
"""

from django.db import models
from datetime import datetime
from django.contrib import admin #добавили использование административного модуля
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Модель данных Блога
class Blog(models.Model):
    title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")
    author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")
    description = models.TextField(verbose_name = "Краткое содержание")
    content = models.TextField(verbose_name = "Полное содержание")
    posted = models.DateTimeField(default = datetime.now(),db_index = True, verbose_name = "Опубликована")
    image = models.FileField(default = 'temp.jpg', verbose_name = "Путь к картинке")

    def get_absolute_url(self):
        return reverse("blogpost", args=[srt(self.id)])             #метод возвращает строку с уникальным интернет-адресом записи

    def __str__(self):                                              #метод возвращает название используемое для представления отдельны запросов
        return self.title

    class Meta:
        db_table = "Posts"                                          #имя таблицы для модели
        ordering = ["-posted"]                                      #порядок сортировки данных в модели
        verbose_name = "статьи блога"                               #имя, под которым модель будет отображаться в административном разделе
        verbose_name_plural = "стать блога"                         #для всех статей

admin.site.register(Blog)

# Модель комментариев
class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    data = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def __str__(self):                                             
        return 'Коментарий %s к %s' % (self.author, self.post)
        
    class Meta:
        db_table = "Comment"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарий для статьи блога"
        ordering = ["-data"]

admin.site.register(Comment)