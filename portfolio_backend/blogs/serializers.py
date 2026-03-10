from rest_framework import serializers
from .models import Category, BlogPost

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
        read_only_fields = ['slug']

class BlogPostSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    author_name = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'author', 'author_name', 
            'category', 'category_name', 'image', 'content', 'status', 
            'created_when', 'updated_at'
        ]
        read_only_fields = ['slug', 'created_when', 'updated_at']