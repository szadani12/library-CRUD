from django.contrib import admin
from library.models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'year', 'price')
    search_fields = ('category',)

admin.site.register(Book, BookAdmin) #PARÂMETROS PARA A PÁGINA DE ADMIN
