from django.urls import path 
from .views import product_detail, product_list, index, about, news
app_name = 'dress'

urlpatterns = [ 
    path('',index, name='index'), 
    path('all/', product_list, name='product_list'),
    path('news/', news, name='news'),
    path('about_as/', about, name='about'),
    path('<slug:category_slug>/', product_list, name='product_category'),    
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
] 