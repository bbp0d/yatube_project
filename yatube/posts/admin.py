from django.contrib import admin
from .models import Group, Post


class GroupAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug', 'description') # Перечисляем поля, которые должны отображаться в админке
    search_fields = ('title',) # Добавляем интерфейс для поиска по тексту постов
    list_filter = ('title',) # Добавляем возможность фильтрации по дате
    empty_value_display = '-пусто-' # Это свойство сработает для всех колонок: где пусто — там будет эта строка 


class PostAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'text', 'pub_date', 'author', 'group') # Перечисляем поля, которые должны отображаться в админке
    search_fields = ('text',) # Добавляем интерфейс для поиска по тексту постов
    list_filter = ('pub_date',) # Добавляем возможность фильтрации по дате
    empty_value_display = '-пусто-' # Это свойство сработает для всех колонок: где пусто — там будет эта строка 
    list_editable = ('group',)

admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)

