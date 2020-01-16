from django.contrib import admin
from .models import Category, News, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_filter = ('name', 'slug')
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name', )}


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'slug', 'image', 'body', 'status')
    list_filter = ('category', 'created', 'status')
    search_fields = ('category', 'title', 'slug')
    prepopulated_fields = {'slug': ('title', )}
    ordering = ('status', )

admin.site.register(Author)
