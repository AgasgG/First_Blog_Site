from datetime import datetime

from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from mysite import settings
from web.models import Publication, Feedbacks


def index(request):
    return render(request, 'index.html')

#15.04.2020_Заменено моделью Publication
#publications_data = [
#{
#        'id': 0,
#        'name': 'Моя первая публикация',
#        'date': datetime.datetime.now(),
#        'text': '''
#        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32. <br></br>The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham.
#        '''
#        },
#{
#        'id': 1,
#        'name': 'Моя вторая публикация',
#        'date': datetime.datetime.now(),
#        'text': '''
#        There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which don't look even slightly believable. If you are going to use a passage of Lorem Ipsum, you need to be sure there isn't anything embarrassing hidden in the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.
#        '''
#        },
#{
#        'id': 2,
#        'name': 'Моя третья публикация',
#        'date': datetime.datetime.now(),
#        'text': '''<h3>Почему он используется?</h3><br></br>Давно выяснено, что при оценке дизайна и композиции читаемый текст мешает сосредоточиться. Lorem Ipsum используют потому, что тот обеспечивает более или менее стандартное заполнение шаблона, а также реальное распределение букв и пробелов в абзацах, которое не получается при простой дубликации "Здесь ваш текст.. Здесь ваш текст.. Здесь ваш текст.." Многие программы электронной вёрстки и редакторы HTML используют Lorem Ipsum в качестве текста по умолчанию, так что поиск по ключевым словам "lorem ipsum" сразу показывает, как много веб-страниц всё ещё дожидаются своего настоящего рождения. За прошедшие годы текст Lorem Ipsum получил много версий. Некоторые версии появились по ошибке, некоторые - намеренно (например, юмористические варианты).
#        '''
#        }]


def publish(request):
    if request.method == 'GET':
        return render(request, 'publish.html')
    else:
        secret = request.POST['secret']
        name = request.POST['name']
        text = request.POST['text']

        if secret != settings.SECRET_KEY:
            return render(request, 'publish.html', {
                'error': 'Неправильный Secret Key!'
            })

        if len(name) == 0:
            return render(request, 'publish.html', {
                'error': 'Пустое имя!'
            })

        if len(text) == 0:
            return render(request, 'publish.html', {
                'error': 'Пустой текст!'
            })

        #publications_data.append({
        #    'id': len(publications_data),
        #    'name': name,
        #    'date': datetime.datetime.now(),
        #    'text': text.replace('\n', '<br>')
        #})
        Publication(
            name=name,
            date=datetime.now(),
            text=text.replace('\n', '<br>')).save()
        return redirect('/publications')


def publications(request):
    return render(request, 'publications.html', {
        #'publications': publications_data #15.04.2020
        'publications': Publication.objects.all()
    })

'''#15.04.2020
def publication(request, number):
    if number < len(publications_data):
        return render(request, 'publication.html', publications_data[number])
    else:
        return redirect('/')
'''
def publication(request, number):
    pubs = Publication.objects.filter(id=number)

    if len(pubs)==1:
        pub = model_to_dict(pubs[0])
        return render(request, 'publication.html', pub)
    else:
        return redirect('/')

#16.04.20 замена models.feedbacks
# feedback_data = [{
#     'id':0,
#     'name': 'Тестовая',
#     'date': 'date',
#     'email' : 'test@mail.ru',
#     'text' : 'Текст обратной связи'
#}]

def contacts(request):
    if request.method == 'GET':
        return render(request, 'contacts.html')
    else:
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']

        if len(name) == 0:
            return render(request, 'contacts.html', {
                'error': 'Пустое имя!'
            })

        if len(email) == 0:
            return render(request, 'contacts.html', {
                'error': 'Пустой адрес!'
            })

        if len(text) == 0:
            return render(request, 'contacts.html', {
                'error': 'Пустой текст!'
            })

#16.04.20 Замена списка на SQL таблицу
        # feedback_data.append({
        #     'id': len(feedback_data),
        #     'name': name,
        #     'date': datetime.now(),
        #     'email': email,
        #     'text': text.replace('\n', '<br>')
        # })
        Feedbacks(
            name=name,
            email=email,
            date=datetime.now(),
            text=text.replace('\n', '<br>')).save()

        return render(request, 'contacts.html', {
            'message': 'Сообщение отправлено!'
        })

def feedbacks(request):
    return render(request, 'feedbacks.html', {
        'feedbacks': feedback_data
    })
