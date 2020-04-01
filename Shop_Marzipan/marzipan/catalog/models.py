from django.db import models

# Create your models here.

class Catalog(models.Model):
    title=models.CharField(max_length=30, verbose_name='Товар')
    content=models.TextField(verbose_name='Описание', null=True, blank=True)
    price=models.FloatField(verbose_name='Цена', blank=True, null=True)
    images= models.CharField(verbose_name='Изображение', max_length=30, default="default title")
    rental = models.BooleanField(verbose_name='Аренда', db_index=True, blank=True)
    published=models.DateTimeField(verbose_name='Публикация', auto_now_add=True, db_index=True)
    category=models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'
        ordering=['-published']

class Category(models.Model):
    name=models.CharField(max_length=20, db_index=True, verbose_name='Название')
    img= models.CharField(max_length=30, verbose_name='Изображение', default="default title")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['name']
    