from django.db import models
from dress.models import Product


class Order(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField('E-Mail')
    address = models.CharField('Адрес', max_length=250)
    postal_code = models.CharField('Индекс', max_length=20)
    country = models.CharField('Страна', max_length=100)
    city = models.CharField('Город', max_length=100)
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Обновление', auto_now=True)
    paid = models.BooleanField('', default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name='items', on_delete=models.CASCADE, verbose_name = 'Заказ')
    product = models.ForeignKey(
        Product, related_name='order_items', on_delete=models.CASCADE, verbose_name = 'Товар')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField('Кол-во', default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
