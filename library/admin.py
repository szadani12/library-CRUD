from django.contrib import admin
from library.models import Book, Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'year', 'price')
    search_fields = ('title',)

admin.site.register(Book, BookAdmin) #PARÂMETROS PARA A PÁGINA DE ADMIN
admin.site.register(Category, CategoryAdmin)
