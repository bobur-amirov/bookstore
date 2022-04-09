from django.contrib import admin

from .models import Book, Category, Language, Author, Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'slug']
    prepopulated_fields = {'slug': ('first_name', 'last_name')}

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ImageInlineModel(admin.TabularInline):
    model = Image

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ImageInlineModel]