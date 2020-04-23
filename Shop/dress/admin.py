from django.contrib import admin
from .models import Category, Product

@admin.register(Category) 
class CategoryAdmin(admin.ModelAdmin): 
   list_display = ['title', 'slug']    
   prepopulated_fields = {'slug': ('title',)}

@admin.register(Product) 
class ProductAdmin(admin.ModelAdmin):    
    list_display = ['title', 'category', 'price', 'available', 'created', 'updated']    
    list_filter = ['available', 'created', 'updated']    
    list_editable = ['price', 'available']    
    prepopulated_fields = {'slug': ('title',)} 
