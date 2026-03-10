from django.contrib import admin
from .models import Category, BlogPost

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # Automatically fills the slug field as you type the name
    prepopulated_fields = {'slug': ('name',)} 
    search_fields = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'status', 'created_when')
    list_filter = ('status', 'category', 'created_when')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    # Add a date hierarchy for easy filtering by date at the top of the admin list
    date_hierarchy = 'created_when' 
    # Make the status editable directly from the list view
    list_editable = ('status',)