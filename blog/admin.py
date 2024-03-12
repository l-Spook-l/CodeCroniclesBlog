from django.contrib import admin
from .models import Post, CategoryPost, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


class CategoryPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


class CommentPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'parent', 'created_at')
    list_display_links = ('id', 'post')
    search_fields = ('post', 'author', 'parent')


admin.site.register(Post, PostAdmin)
admin.site.register(CategoryPost, CategoryPostAdmin)
admin.site.register(Comment, CommentPostAdmin)
