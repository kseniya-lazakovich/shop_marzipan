from django.db import models
from django.urls import reverse


class Post(models.Model):
    """ Статьи """
    title = models.CharField('Заголовок', max_length=200, db_index=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to="blog/", blank=True)
    slug = models.SlugField(max_length=100, db_index=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('blog:blog', args=[self.slug])


class Comment(models.Model):
    """ Комментарии """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments', verbose_name='Статья')
    name = models.CharField('Имя', max_length=80)
    email = models.EmailField('Email')
    body = models.TextField('Комент')
    created = models.DateTimeField('Создание', auto_now_add=True)
    updated = models.DateTimeField('Обновление', auto_now=True)
    active = models.BooleanField('Активность', default=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
