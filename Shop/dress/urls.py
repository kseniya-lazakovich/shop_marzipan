from django.urls import path 
from .views import product_detail, product_list, index
app_name = 'dress'

urlpatterns = [    
    path('',index, name='index'), 
    path('all/', product_list, name='product_list'),  
    path('<slug:category_slug>/', product_list, name='product_category'),    
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'), 
] 