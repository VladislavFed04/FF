"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from.models import Comment   
from.models import Blog


class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Пароль'}))
class AnketaForm(forms.Form):
    name = forms.CharField(label='Любимый игрок?', min_length=1, max_length=254)
    club = forms.CharField(label='Ваш любимый футбольный клуб или национальная сборная?', min_length=1, max_length=254)
    age = forms.CharField(label='Ваш возраст?', min_length=1, max_length=4)
    gender = forms.ChoiceField(label='Ваш пол?',
                                   choices=[('1','Мужчина'),('2','Женщина')],
                                   widget=forms.RadioSelect, initial=1)
    broadcast = forms.ChoiceField(label='Как часто вы смотрите трансляции футбольных матчей?',
                                 choices=(('1','Постоянно'),
                                          ('2','Раз в день'),
                                          ('3','Раз в неделю'),
                                          ('4','Никогда(Alt+F4)')), initial=1)
    notice = forms.BooleanField(label='Хотите получать уведомления?',
                                required=False)
    email = forms.EmailField(label='Ваш e-mail', min_length=2, max_length=20)
    message = forms.CharField(label='О себе или пожелания сайту', widget=forms.Textarea(attrs={'rows':12,'cols':20}) )
 

class CommentForm (forms.ModelForm):

        class Meta:
            model = Comment                     #используемая модель
            fields = ('text',)                  #требуется заполнять только поле text
            label = {'text' : "Комментарий"}    #метка к полю формы text

class BlogForm (forms.ModelForm):

        class Meta:
            model = Blog        #используемая модель
            fields = ('title', 'description', 'content', 'posted', 'author', 'image',)
            labels = {'title': "Заголовок", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата", 'author': "Автор"}

