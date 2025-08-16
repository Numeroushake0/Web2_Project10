from django.contrib import admin
from .models import Author, Quote, Tag

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'born')
    search_fields = ('name',)

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('text_short', 'author')
    list_filter = ('author', 'tags')
    search_fields = ('text',)

    def text_short(self, obj):
        return obj.text[:50] + '...'
    text_short.short_description = 'Quote'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
