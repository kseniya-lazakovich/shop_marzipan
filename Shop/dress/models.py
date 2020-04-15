from django.db import models
from datetime import date

class Category(models.Model):
    ''' Категория '''
    title = models.CharField('Категория', max_length=50)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Parameters(models.Model):
    ''' Параметры '''
    title = models.CharField('Параметры', max_length=50)
    url = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметры'

class Item(models.Model):
    ''' Товары '''
    title = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to="item/")
    price = models.PositiveSmallIntegerField('Цена', default=0)
    parameters = models.ManyToManyField(Parameters, verbose_name = 'Параметр', related_name="model_parameter")
    published = models.DateField('Дата публикации', default = date.today)
    category = models.ForeignKey(Category, verbose_name = 'Категория', on_delete=models.SET_NULL, null= True)
    url = models.SlugField(max_length=100, unique=True)
    draft = models.BooleanField('Черновик', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Articles(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Содержание')
    published = models.DateTimeField('Дата публикации', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'