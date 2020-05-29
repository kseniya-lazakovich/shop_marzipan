from django.shortcuts import render, redirect
from .models import OrderItem, Order
from django.core.mail import send_mail
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse


def order_created(order_id):
    """Задача отправки email-уведомлений при успешном оформлении заказа."""
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Дорогой {},\n\nВаш заказ оформлен и принят в обработку.\n'\
              'Номер заказа №{}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])
    return mail_sent


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item[
                    'price'], quantity=item['quantity'])
            cart.clear()
            order_created(order.id)
            request.session['order_id'] = order.id
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})
