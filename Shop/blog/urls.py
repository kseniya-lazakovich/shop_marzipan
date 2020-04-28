from django.urls import path
from .views import blog_index, post_detail
app_name='blog'

urlpatterns = [
    path('', blog_index, name='blog' ),
    path('<slug:slug>/', post_detail, name='post_detail'),
]