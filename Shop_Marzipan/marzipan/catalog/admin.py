from django.contrib import admin
from .models import Catalog, Category

# Register your models here.
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price','images', 'rental', 'published','category')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'rental')
admin.site.register(Category)
admin.site.register(Catalog, CatalogAdmin)