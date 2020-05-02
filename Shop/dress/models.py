from django.db import models
from django.urls import reverse


class Category(models.Model):
    ''' Категория '''
    title = models.CharField('Категория', max_length=50)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('main:product_category', args=[self.slug])


class Product(models.Model):
    ''' Товары '''
    title = models.CharField('Имя', max_length=100, db_index=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Изображение', upload_to="item/", blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category, verbose_name='Категория', on_delete=models.CASCADE, related_name='products')
    slug = models.SlugField(max_length=100, db_index=True)
    available = models.BooleanField(default=True, verbose_name='В наличии')
    created = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(
        auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('title',)
        index_together = (('id', 'slug'),)

    def get_absolute_url(self):
        return reverse('main:product_detail', args=[self.id, self.slug])
