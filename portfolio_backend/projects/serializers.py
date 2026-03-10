from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'category', 'description', 
            'my_contributions', 'image', 'tags', 'code_link', 
            'demo_link', 'is_published', 'created_when', 'order'
        ]
        read_only_fields = ['id', 'slug', 'created_when']