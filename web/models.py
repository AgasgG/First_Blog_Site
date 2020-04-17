from django.db import models

class Publication(models.Model):
    name = models.CharField(max_length=120)
    date = models.DateTimeField()
    text = models.TextField()

'''
Как работает миграция данных:
Берётся текущее состояние базы (изначально пустую)
Смотрит на все модели которые были созданы (Publication)
Сравнивает код и состояние базы
Создаёт файлик в котором фиксирует изменения
Команда: python manage.py makemigrations web (второй раз можно запускать уже "python manage.py makemigrations"
Выполнит создание папки migrations в которой сохраняет файлы с изменениями БД
Команда: python manage.py migrate выполнит миграцию данныю в БД (все изменения созданные с помощью makemigrations)
'''

class Feedbacks(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()
    email = models.CharField(max_length=50)
    text = models.TextField()