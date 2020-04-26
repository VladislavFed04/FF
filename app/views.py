"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .forms import AnketaForm 
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Comment                                         #использование модели комметариев
from .forms import CommentForm                                      # использование формы ввода комментария
from django.db import models
from .forms import Blog
from .forms import BlogForm
#from .forms import newpost

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Возможность связаться с нами',
            
            'year':datetime.now().year,
        }
    )

def blog(request):
    """Renders the blog page."""
    assert isinstance(request, HttpRequest)

    posts = Blog.objects.all() # запрос на выбор всех статей блога из модели
    return render(
        request,
         'app/blog.html',
        {
            'title':'Блог',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blogpost page."""
    assert isinstance(request, HttpRequest)
    post_1 = Blog.objects.get(id=parametr)                      # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)           #запрос на выбор всех комментариев статьи

    if request.method == "POST":                                #после отправки данных на сервер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)                 
            comment_f.author = request.user                     #добавлям(этого поля нет в форме)
            comment_f.date = datetime.now()                     #добавляем в модель комментария(Comment)
            comment_f.post = Blog.objects.get(id=parametr)      #добавляем в модель комментария
            comment_f.save()                                    #созраняем изменения после добавления полей

        return redirect('blogpost', parametr=post_1.id)     #переадресация на ту же страницу
    else:
        form = CommentForm()                                     #создание формы для ввода комментария
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments,                                #передача всех комментраиев к данный статье в шаблон веб-страницы
            'form': form,                                        #передач формы добавления комментария в шаблон веб-страницы
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'История возникновения футбола',
            'message':'',
            'year':datetime.now().year,
        }
    )

def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужчина', '2': 'Женщина'}
    broadcast = {'1': 'Постоянно' , '2': 'Раз в день', '3': 'Раз в неделю', '4': 'Никогда' }
    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['club'] = form.cleaned_data['club']
            data['age'] = form.cleaned_data['age']
            data['gender'] = gender[ form.cleaned_data['gender'] ]
            data['broadcast'] = broadcast[ form.cleaned_data['broadcast'] ]
            if(form.cleaned_data['notice'] == True):
                data['notice'] = 'Да'
            else:
                data['notice'] = 'Нет'
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
         form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form':form,
            'data':data
            }
        )

def links(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/links.html',
        {
            'title':'Интересные ресурсы',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def registration(request):
    """Renders the registration page."""

    if request.method == "POST":
        regform = UserCreationForm(request.POST)            # после отправки формы
        if regform.is_valid():
            reg_f = regform.save(commit=False)
            reg_f.is_staff = False                          # запрещен вход в административный раздел
            reg_f.is_active = True                          # активный пользователь
            reg_f.is_superuser = False                      # не является суперпользователем
            reg_f.date_joined = datetime.now()              # дата регистрации
            reg_f.last_login = datetime.now()               # дата последнейй авторизации

            regform.save()                                  # сохраненяем изменения после добавления полей

            return redirect('home')                         # переадресация на главную страницу после
    else:
        regform = UserCreationForm()                # создание объекта формы для вводы данных
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html' ,
        {
            'regform': regform,                         # передача формы в шаблон веб-страницы

            'year' :datetime.now().year,
        }
    )

def newpost(request):
    """Renders the newpost page."""

    if request.method == "POST":                        #после отправки формы(ура тут есть комментарии)
        blogform = BlogForm(request.POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()

            blog_f.save()

            return redirect('blog')
    else:
        blogform = BlogForm()

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'blogform': blogform,
            
            'year': datetime.now().year,
        }
    )
def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'year':datetime.now().year,
        }
    )