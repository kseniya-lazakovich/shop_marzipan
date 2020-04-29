from django.urls import path
from .views import blog_list, post_detail
app_name='blog'

urlpatterns = [
    path('', blog_list, name='blog_list' ),
    path('<slug:slug>/', post_detail, name='post_detail'),
]